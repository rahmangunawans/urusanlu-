import requests
from requests.structures import CaseInsensitiveDict

url = "https://www.netflix.com/api/aui/pathEvaluator/web/%5E2.0.0"

headers = CaseInsensitiveDict()
headers["authority"] = "www.netflix.com"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
headers["content-type"] = "application/x-www-form-urlencoded"
headers["sec-ch-ua-mobile"] = "?0"
headers["accept"] = "*/*"
headers["origin"] = "https://www.netflix.com"
headers["sec-fetch-site"] = "same-origin"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-dest"] = "empty"
headers["referer"] = "https://www.netflix.com/signup/regform"
headers["accept-language"] = "en-US,en;q=0.9"
headers["cookie"] = "nfvdid=BQFmAAEBEFbbJ1MSzJS-RKkHYbIMoq1A-yzMzWkmSytjBpDCJ6lJswIIaIpmO06lbGpgN6npT4qjaA0aYYKjlQ71AgrmQyv0XaMRq2ugkIjWXObt73CPNA%3D%3D; memclid=9a57e95e-7437-4223-968c-3f0b45c69ab9; SecureNetflixId=v%3D2%26mac%3DAQEAEQABABSBk95rgKlC2KWbe1RrX2P50XGV9ArrAMw.%26dt%3D1617974987616; NetflixId=v%3D2%26ct%3DBQAOAAEBED2NRPtbk6QlDYmYXaMkV1CBINuqlp9PGgar9HTkg_XWPT1pIBuH1GQuE_AoSlid9YZznRKPvJq1yUu-fxfRorGAw5CByEVp5cXfo8sHbmiPRn2X5KfcgblRin4cZ1GSupsA94ObtNXLYyGnt4LcGEJnXWpc0Py2cCamM-FiEDGFbPMtecC9oJWPxFgqRaqUxi9QIB_AHqcYfpcg9dj0bebmPVjrdi9CiYjC_EZ1aZkp7XOrm3CG-mkldsbrOifQ41OF0i35bDWbDajy1AAgVaIHovX9rE670IWmsO_T6AkXHb7_qiNYn3_zzYnWLa8E5QeUDzMiY5KL_gK9QrC6Bgi7OoaMBxo_QnkS-XBi22diZym-0gWUShwUzX2IyinsCBS0huFx3DcQnGL6JoAlqUlNIA..%26bt%3Ddev%26mac%3DAQEAEAABABRE3-IoUDbfWdQn4z-JcFzUNSWMmOinyxo.; flwssn=4f8939a5-909a-4efd-9714-1817f9f1a38b; clSharedContext=e656d3a5-c21c-4546-b17c-29f75b1d3b8a; cL=1617978983775%7C16179789836891327%7C161797898321362534%7C%7C4%7Cnull; OptanonConsent=isIABGlobal=false&datestamp=Fri+Apr+09+2021+21%3A36%3A24+GMT%2B0700+(Western+Indonesia+Time)&version=6.6.0&consentId=6f441100-168f-417e-82b7-39684f0263b7&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&hosts=H1%3A1%2CH2%3A1%2CH12%3A1%2CH13%3A1%2CH27%3A1%2CH28%3A1%2CH30%3A1&AwaitingReconsent=false; sawContext=true"

params = (
    ('landingURL', '/signup/regform'),
    ('landingOrigin', 'https://www.netflix.com'),
    ('inapp', 'false'),
    ('languages', 'en-ID'),
    ('netflixClientPlatform', 'browser'),
    ('flow', 'signupSimplicity'),
    ('mode', 'registration'),
    ('method', 'call'),
    ('falcor_server', '0.1.0'),
    ('callPath', '["aui","moneyball","next"]'),
)
data = {
  'param': '{"action":"registerOnlyAction","fields":{"email":{"value":"suzannemjwas@hotmail.com"},"password":{"value":"x"},"emailPreference":{"value":false},"previousMode":"registrationWithContext"}}',
  'allocations': '{"31483":2,"35894":2,"36518":9,"36520":2}',
  'esn': 'NFCDCH-02-H4Z88F7AEM3P85K0KH77Q1K7WFX3FF',
  'authURL': '1617978982456.plu/T8xRfdBEQjwyX3z+STpcqOM='
}

resp = requests.post(url, headers=headers, data=data, params=params)

print(resp.text)

