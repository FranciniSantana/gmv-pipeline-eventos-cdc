import pandas as pd
from datetime import datetime

# ================================
# PURCHASE (CDC EVENTS)
# ================================

purchase_data = [
    {
        "purchase_id": 55,
        "buyer_id": 15947,
        "prod_item_id": 1,
        "order_date": "2023-01-20",
        "release_date": "2023-01-20",
        "producer_id": 85252,
        "purchase_partition": 5,
        "prod_item_partition": 5,
        "purchase_total_value": 50.00,
        "purchase_status": "approved",
        "transaction_datetime": "2023-01-20 22:00:00",
        "transaction_date": "2023-01-20"
    },
    {
        "purchase_id": 66,
        "buyer_id": 369798,
        "prod_item_id": 5,
        "order_date": "2023-01-25",
        "release_date": "2023-01-20",
        "producer_id": 963963,
        "purchase_partition": 6,
        "prod_item_partition": 0,
        "purchase_total_value": 2400.00,
        "purchase_status": "approved",
        "transaction_datetime": "2023-01-26 00:01:00",
        "transaction_date": "2023-01-26"
    },
    {
        "purchase_id": 69,
        "buyer_id": 147,
        "prod_item_id": 98736,
        "order_date": "2023-02-20",
        "release_date": None,
        "producer_id": 96967,
        "purchase_partition": 7,
        "prod_item_partition": 6,
        "purchase_total_value": 2000.00,
        "purchase_status": "pending",
        "transaction_datetime": "2023-02-26 03:00:00",
        "transaction_date": "2023-02-26"
    },
    # evento CDC corrigindo release_date depois
    {
        "purchase_id": 69,
        "buyer_id": 147,
        "prod_item_id": 98736,
        "order_date": "2023-02-20",
        "release_date": "2023-03-01",
        "producer_id": 96967,
        "purchase_partition": 7,
        "prod_item_partition": 6,
        "purchase_total_value": 2000.00,
        "purchase_status": "approved",
        "transaction_datetime": "2023-03-12 07:00:00",
        "transaction_date": "2023-03-12"
    }
]

purchase_df = pd.DataFrame(purchase_data)

# ================================
# PRODUCT ITEM (CDC EVENTS)
# ================================

product_item_data = [
    {
        "prod_item_id": 1,
        "prod_item_partition": 5,
        "product_id": 696969,
        "item_quantity": 10,
        "purchase_value": 50.00,
        "transaction_datetime": "2023-01-20 22:02:00",
        "transaction_date": "2023-01-20"
    },
    {
        "prod_item_id": 5,
        "prod_item_partition": 0,
        "product_id": 808080,
        "item_quantity": 120,
        "purchase_value": 2400.00,
        "transaction_datetime": "2023-01-25 23:59:59",
        "transaction_date": "2023-01-25"
    },
    {
        "prod_item_id": 98736,
        "prod_item_partition": 6,
        "product_id": 377377,
        "item_quantity": 2,
        "purchase_value": 2000.00,
        "transaction_datetime": "2023-02-26 03:00:00",
        "transaction_date": "2023-02-26"
    }
]

product_item_df = pd.DataFrame(product_item_data)

# ================================
# PURCHASE EXTRA INFO (CDC EVENTS)
# ================================

purchase_extra_info_data = [
    {
        "purchase_id": 55,
        "purchase_partition": 5,
        "subsidiary": "nacional",
        "transaction_datetime": "2023-01-23 00:05:00",
        "transaction_date": "2023-01-23"
    },
    {
        "purchase_id": 66,
        "purchase_partition": 6,
        "subsidiary": "internacional",
        "transaction_datetime": "2023-01-25 23:59:59",
        "transaction_date": "2023-01-25"
    },
    {
        "purchase_id": 69,
        "purchase_partition": 7,
        "subsidiary": "nacional",
        "transaction_datetime": "2023-02-28 01:00:00",
        "transaction_date": "2023-02-28"
    },
    # CDC correction
    {
        "purchase_id": 69,
        "purchase_partition": 7,
        "subsidiary": "internacional",
        "transaction_datetime": "2023-03-12 07:00:00",
        "transaction_date": "2023-03-12"
    }
]

purchase_extra_info_df = pd.DataFrame(purchase_extra_info_data)

# ================================
# SAVE CSV FILES
# ================================

purchase_df.to_csv("data/purchase.csv", index=False)
product_item_df.to_csv("data/product_item.csv", index=False)
purchase_extra_info_df.to_csv("data/purchase_extra_info.csv", index=False)

print("CSV files generated successfully!")
