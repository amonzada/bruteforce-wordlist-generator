import datetime
from .core.common_config import config, logging

def date_based_generator(output_file: str = "dates.txt") -> None:
    date_formats = [
        "%d%m%Y", "%m%d%Y", "%Y%m%d", "%d%m%y", "%m%d%y",
        "%H%M%S", "%d%m", "%m%Y", "%y%m", "%Y%m"
    ]
    
    try:
        dates = []
        for year in config.common_years:
            for month in range(1, 13):
                for day in range(1, 31):
                    try:
                        date_obj = datetime.date(int(year), month, day)
                        for fmt in date_formats:
                            dates.append(date_obj.strftime(fmt))
                    except ValueError:
                        continue
        
        with open(output_file, "w") as f:
            for d in set(dates):
                f.write(d + "\n")
        
        logging.info(f"Datas geradas: {output_file}")
    except Exception as e:
        logging.error(f"Erro na geração de datas: {str(e)}")

if __name__ == "__main__":
    date_based_generator()