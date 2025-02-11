import requests

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/132.0.0.0 Safari/537.36",
    "Referer": "https://codeforces.com/problemset/submit",
    "Origin": "https://codeforces.com",
}

cookies = {
    "lastOnlineTimeUpdaterInvocation": "1738632986208",
    "_ga": "GA1.1.1282273021.1738507004",
    "_ga_K230KVN22K": "GS1.1.1738507004.1.1.1738507127.0.0.0",
    "X-User": "",
    "JSESSIONID": "49BCC6C316450E9BED6247FC78FDB4BE",
    "39ce7": "CFUUd8ZV",
    "pow": "d252f088f4eb62c23c759546fb20846e08e0d575",
    "evercookie_cache": "puwyswf8c4fwumfcyn",
    "evercookie_etag": "puwyswf8c4fwumfcyn",
    "evercookie_png": "puwyswf8c4fwumfcyn",
    "70a7c28f3de": "puwyswf8c4fwumfcyn",
    "X-User-Sha1": "64a39362696275a83b8d4bc65c0ec76fb27e9364",
    "lastOnlineTimeUpdaterInvocation": "1738630561687",
    "cf_clearance": "8a8W0gj8C6_8shFmTxmUfsyBbu6SIAm9C45u0YEW020-1738631485-1.2.1.1-xEm9XJBUXp2ysWR2KDOJkN7gdTD86qizQ71zQnEtxzEoysP.QBIHcn0TCgeby0HhrDVwACk8gsZJdYsLtlpFPC.eNp8mpa8mA1BMU7dF4ArifIsSgBm55WXZfecbQOA3EsMnYUSGEoFTWJuUW6fLHoXg2mPxeV73ph3CQlBXOU.w2i_hs7OVs6O4XjNPfDVHwU1W5uxtawPvmk44PZc1f0ebPdTrem6ycsoTyHUpNDCYmx9JdXrmBzw0EYFlVNIFbFyOowMGRLnhaFaS0F.0.Z9UFMTXK63I0fC87rOhecQ5gCNfYuI4S.GjKE316Y.HdSqmtGi.ejQ5z_XGBNm9hw"
}

session.cookies.update(cookies)

while True:
    csrf_token = input("enter csrf: ")
    ftaa = input("enter ftaa: ")
    bfaa = input("enter bfaa: ")
    contest = input("enter contest: ")
    problem = input("enter problem: ")

    url = f"https://codeforces.com/problemset/submit?csrf_token={csrf_token}"


    payload = {
        "csrf_token": csrf_token,
        "ftaa": ftaa,
        "bfaa": bfaa,
        "action": "submitSolutionFormSubmitted",
        "contestId": contest,
        "submittedProblemIndex": problem,
        "programTypeId": "70",
        "source": "fortnite",
        "tabSize": "4",
        "sourceFile": "",
        "_tta": "364"
    }

    response = session.post(url, data=payload, headers=headers)

    print("Status code:", response.status_code)
    print("Final URL:", response.url)
    print("Response body snippet:", response.text)

