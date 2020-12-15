-- Vendors table (for all vendors list.)
CREATE TABLE IF NOT EXISTS vendors (
    id integer PRIMARY KEY,
    product text,
    vendor text NOT NULL
);

-- Products plus vendor table.
CREATE TABLE IF NOT EXISTS products (
    id integer PRIMARY KEY,
    product text NOT NULL,
    vendor text NOT NULL
)

-- Last 30 table. 
CREATE TABLE IF NOT EXISTS latest (
    
)