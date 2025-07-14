from SingleEndpointRouter import Server

endpoints = [
    "http://10.156.22.177:3000",
    "http://10.156.22.177:3101",
    "http://10.156.22.177:3103",
    "http://10.156.22.177:3105",
]

app = Server(endpoints)
app.clean_cache()  # Example: Clean the cache before running the server
app.run(debug=False, host="0.0.0.0", port=8000)
