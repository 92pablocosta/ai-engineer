from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def list_products(
    category: str | None = None,
    limit: int = 10
):
    if category is None:
        return {
            "message": "No category provided.",
            "limit": limit
        }

    return {
        "message": f"Listing products from category: {category}",
        "limit": limit
    }
