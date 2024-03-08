import os
import re
import requests
from typing import Dict, List, Tuple
 
import osc_ingest_trino as osc
osc.load_credentials_dotenv()

import ITR
from ITR.interfaces import EScope, IEmissionsRealization, IHistoricEmissionsScopes
from ITR.data.osc_units import Quantity

url = "https://nzdpu.com/wis/coverage/companies/Q9MAIUP40P25UFBFG033/history"
headers = {"accept": "application/json", "access_key": os.environ["NZDPU_API_KEY"],}
data = {}  # for requests.post
 
company_leis_nomatch = [
    "2NUNNB7D43COUIRE5295",
    "3SOUA6IRML7435B56G12",
    "J3WHBG0MTS7O8ZVMDC91",
    "549300SVYJS666PQJH88",
    "CE5OG6JPOZMDSA0LAQ19",
    "5493006W3QUS5LMH6R84",
    "549300MQYQ9Y065XPR71",
    "3MGELCRSTNSAMJ962671",
    "549300LKH11TFCJLZK20",
    "549300MQYQ9Y065XPR71",
    "3MGELCRSTNSAMJ962671",
    "549300LKH11TFCJLZK20",
    "549300NNLSIMY6Z8OT86",
    "5493009ML300G373MZ12",
    "1B4S6S7G0TW5EE83BO58",
    "DX6I6ZD3X5WNNCDJKP85",
    "5493002H80P81B3HXL31",
    "549300TM2WLI2BJMDD86",
    "549300IA9XFBAGNIBW29",
    "549300OQS2LO07ZJ7N73",
    "ILUL7B6Z54MRYCF6H308",
    "4XM3TW50JULSLG8BNC79",
    "549300PGTHDQY6PSUI61",
    "SJ7XXD41SQU3ZNWUJ746",
    "254900YDV6SEQQPZVG24",
    "JJ8FWOCWCV22X7GUPJ23",
    "UMI46YPGBLUE4VGNNT48",
    "35380065QWQ4U2V3PA33",
    "549300D8GOWWH0SJB189",
    "3BPWMBHR1R9SHUN7J795",
    "549300GGJCRSI2TIEJ46",
    "8YQ2GSDWYZXO2EDN3511",
    "TWSEY0NEDUDCKS27AH81",
    "5493003JOBJGLZSDDQ28",
    "GJOUP9M7C39GLSK9R870",
    "988400E5HRVX81AYLM04",
    "9N3UAJSNOUXFKQLF3V18",
    "PBBKGKLRK5S5C0Y4T545",
    "549300FC3G3YU2FBZD92",
    "549300HGGKEL4FYTTQ83",
    "549300Y7C05BKC4HZB40",
    "529900QG4KU23TEI2E46",
    "549300QZTZWHDE9HJL14",
    "JNLUVFYJT1OZSIQ24U47",
    "NQZVQT2P5IUF2PGA1Q48",
    "549300IGLYTZUK3PVP70",
    "1WRCIANKYOIK6KYE5E82",
    "LGJNMI9GH8XIDG5RCM61",
    "549300UGKOFV2IWJJG27",
    "XRZQ5S7HYJFPHJ78L959",
    "54930033SBW53OO8T749",
    "I1BZKREC126H0VB1BL91",
    "0T6SBMK3JTBI1JR36794",
    "549300UGKOFV2IWJJG27",
    "XRZQ5S7HYJFPHJ78L959",
    "54930033SBW53OO8T749",
    "0T6SBMK3JTBI1JR36794",
    "549300UGKOFV2IWJJG27",
    "549300XNOLX5GIOSO108",
    "213800LH1BZH3DI6G760",
    "VA8TZDWPEZYU430RZ444",
    "549300I7ROF15MAEVP56",
    "BUCRF72VH5RBN7X3VL35",
    "5493001871EE1F4JHK38",
    "353800PFUKP5ONPJNZ86",
    "3BNYRYQHD39K4LCKQF12",
    "IM7X0T3ECJW4C1T7ON55",
    "5493000J801JZRCMFE49",
    "5493003RZQYJM7QGNE15",
    "5586006WD91QHB7J4X50",
    "21380068P1DRHMJ8KU70",
    "2138009UNXTD8EYS5M35",
    "988400PXP70BWVSJVF07",
    "EVK05KS7XY1DEII3R011",
    "5299004EMJ3R4RVR5Y75",
    "529900S21EQ1BO4ESM68",
    "5299006UDSEJCTTEJS30",
    "52990016II9MJ2OSWA10",
    "529900KDAQXRLFTJYL75",
    "529900M5G5HGXW4Z4S17",
    "529900SEH9QK8ZZDCQ89",
    "5299005MZ4WZECVATV08",
    "549300Q8LSNHAVWBNI21",
    "213800EFQXH43HMGJL59",
    "529900JSFZ4TS59HKD79",
    "549300OX0Q38NLSKPB49",
    "549300W77ER6BVTNSK57",
    "549300IX8SD6XXD71I78",
    "529900JSFZ4TS59HKD79",
]
company_leis = [
    "PUSS41EMO3E6XXNV3U28",
    "8R95QZMKZLJX5Q2XR704",
    "W9NG6WMZIYEU8VEDOG48",
    "LAXUQCHT4FH58LRZDY46",
    "5QK37QC7NWOJ8D7WVQ45",
    "529900GB7KCA94ACC940",
    "549300X3UK4GG3FNMO06",
    "20S05OYHG0MQM4VUIC57",
    "549300KP43CPCUJOOG15",
    "CT4UIJ3TUKGYYHMENQ17",
    "LZ2C6E0W5W7LQMX5ZI37",
]

# Companies without LEIs; Alas, none covered by NZDPU
company_names = [
    "Koninklijke",
    "L'Oreal",
    "Givaudan",
    "BASF",
    "Arkema",
    "Linde",
    "Nolato",
    "Synthomer",
    "LG H&H",
    "Covestro",
    "Inter Parfums",
    "Borregaard",
    "Symrise",
    "Tokai Carbon",
    "LG Chem",
    "Shiseido",
    "Shin-Etsu Chemical",
]
# url = f"https://nzdpu.com/wis/external/search?name=f{comapny_name}&start=0&limit=10"

headers = {"accept": "application/json", "access_key": os.environ["NZDPU_API_KEY"],}

def get_nzdpu_historic_scopes(lei: str) -> IHistoricEmissionsScopes:
    response = requests.get(
        f"https://nzdpu.com/wis/coverage/companies/{lei}/history",
        headers=headers,
    )
    if response.status_code == 200:
        result = response.json()
        history = result["history"]
        scope_lists = { '1': [], '2': [], '3': [] }
        for h_year in history:
            year = h_year["reporting_year"]
            vals = h_year["submission"]["values"]
            units = h_year["submission"]["units"]
            for k, v in units.items():
                if v is None or type(v) is list:
                    continue
                if k.endswith("_ghg") and vals[k] > 0 and (match := re.match(r".*_([123])_", k)):
                    # FIXME: the following collects both market-based and location-based S2 emissions
                    scope_lists[match.group(1)].append(
                        IEmissionsRealization(year=reporting_year, value=Quantity(vals[k], units[k]))
                    )
        return IHistoricEmissionsScopes(
            S1=scope_lists['1'],
            S2=scope_lists['2'],
            S3=scope_lists['3'],
        )
    else:
        print("Request failed with status code:", response.status_code)
        raise ValueError
