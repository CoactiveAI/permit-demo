Run the Permit PDP locally with Docker:
```
docker run -it \
  -p 7766:7000 \
  --env PDP_API_KEY=<your-permit-api-key> \
  --env PDP_DEBUG=True \
  permitio/pdp-v2:0.8.1
```

Create a .env file with these secrets:
```
PERMIT_ORG_ID=<an existing org in your Permit project>
PERMIT_SDK_KEY=<the Permit SDK key>
```
You may also wish to update the values of `PERMIT_PROJECT` and `PERMIT_PDP_URL` in src/config.ts.

Set up the test
```
just install
```

Run the test
```
just test
```
