# tokenizer
Simple python script to save Stone Portal personified user token to clipboard

## Setup

Set environment variables
- API_PRD_URL
- API_STG_URL
- USER_EMAIL
- USER_PRD_PASSWORD
- USER_STG_PASSWORD
- STONECODE

```bash
pip install -r requirements.txt
python tkn.py {stonecode} {environ}
```
Both `{stonecode}` and `{environ}` are optional.
`{environ}` options are `prd` or `stg` (or whatever you declare on your env vars. Example: if you define a `API_DEV_URL` and a `API_DEV_PASSWORD`, you would de able to pass `dev` as environ).

The api token is now copied to your clipboard, just paste it somewhere safe!