import requests
import logging
from typing import Dict, Any, List
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv


class FotoMonitoreoAPIClient:
    BASE_URL = "https://app.fotomonitoreo.cl/visor/"

    def __init__(self, csrf_token: str):
        self.csrf_token = csrf_token
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie": f"csrftoken={csrf_token}",
                "Origin": "https://app.fotomonitoreo.cl",
                "Referer": "https://app.fotomonitoreo.cl/",
                "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"macOS"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
                "X-Csrftoken": csrf_token,
                "X-Requested-With": "XMLHttpRequest",
            }
        )

    def _make_request(
        self, method: str, endpoint: str, payload: Dict[str, Any] = {"": None}
    ) -> Dict[str, Any]:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            if method == "GET":
                response = self.session.get(url)
            elif method == "POST":
                response = self.session.post(url, data=payload)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")
            return {"error": str(e)}

    def get_regiones(self) -> Dict[str, Any]:
        return self._make_request("GET", "regiones/")

    def get_unidades_by_region(self, codigo_region: str) -> Dict[str, Any]:
        return self._make_request(
            "POST", "unidades_by_region/", {"codigo_region": codigo_region}
        )

    def get_years_by_unidad(self, codigo_unidad: str) -> Dict[str, Any]:
        return self._make_request(
            "POST", "year_by_unidad/", {"codigo_unidad": codigo_unidad}
        )

    def get_especies_by_unidad_year(
        self, codigo_unidad: str, year: str
    ) -> Dict[str, Any]:
        return self._make_request(
            "POST",
            "especie_by_unidadyear/",
            {"codigo_unidad": codigo_unidad, "year": year},
        )

    def get_grillas_by_year_geojson(
        self, codigo_unidad: str, year: str
    ) -> Dict[str, Any]:
        return self._make_request(
            "POST",
            "grillas_by_year_geojson/",
            {"codigo_unidad": codigo_unidad, "year": year},
        )


def process_grilla(
    unidad: Dict[str, Any], year: Dict[str, Any], grilla: Dict[str, Any]
) -> List[str]:
    return [
        unidad["codigo"],
        year["year"],
        grilla["properties"]["cod_grilla"],
        grilla["properties"]["gdrive_url"],
    ]


def get_all_gdrive(csrf_token: str):
    client = FotoMonitoreoAPIClient(csrf_token)
    results = []

    regiones = client.get_regiones()

    with ThreadPoolExecutor(max_workers=5) as executor:
        region_futures = {
            executor.submit(client.get_unidades_by_region, region["codigo"]): region
            for region in regiones["regiones"]
        }

        for region_future in as_completed(region_futures):
            unidades = region_future.result()

            unidad_futures = {
                executor.submit(client.get_years_by_unidad, unidad["codigo"]): unidad
                for unidad in unidades["unidades"]
            }

            for unidad_future in as_completed(unidad_futures):
                unidad = unidad_futures[unidad_future]
                years = unidad_future.result()

                year_futures = {
                    executor.submit(
                        client.get_grillas_by_year_geojson,
                        unidad["codigo"],
                        year["year"],
                    ): (unidad, year)
                    for year in years["years"]
                }

                for year_future in as_completed(year_futures):
                    unidad, year = year_futures[year_future]
                    grillas = year_future.result()

                    for grilla in grillas["features"]:
                        results.append(process_grilla(unidad, year, grilla))

    return results


def create_csv_file(data: List[List[str]], filename: str = "fotomonitoreo_data.csv"):
    headers = ["codigo_unidad", "year", "cod_grilla", "gdrive_url"]

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)

    logging.info(f"CSV file '{filename}' has been created successfully.")


def main():
    logging.basicConfig(level=logging.INFO)
    csrf_token = "IuimajLdEXNSXkOKTz382z6zotowMFf7"

    results = get_all_gdrive(csrf_token)
    create_csv_file(results)


if __name__ == "__main__":
    main()
