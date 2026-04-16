CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE,
    email VARCHAR(150) UNIQUE,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) DEFAULT 'shopper',
    is_verified BOOLEAN DEFAULT FALSE,
    avatar_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    icon_url TEXT,
    parent_id UUID REFERENCES categories(id)
);

CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(150) NOT NULL,
    description TEXT,
    category_id UUID REFERENCES categories(id),
    unit VARCHAR(50),
    image_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE merchants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    business_name VARCHAR(150) NOT NULL,
    description TEXT,
    market_name VARCHAR(150),
    address TEXT,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    is_verified BOOLEAN DEFAULT FALSE,
    badge VARCHAR(20) DEFAULT 'none',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE price_reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_id UUID REFERENCES products(id) ON DELETE CASCADE,
    reported_by UUID REFERENCES users(id),
    merchant_id UUID REFERENCES merchants(id),
    price DECIMAL(12,2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'NGN',
    quantity VARCHAR(50),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    location_name VARCHAR(200),
    is_verified BOOLEAN DEFAULT FALSE,
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE price_confirmations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    price_report_id UUID REFERENCES price_reports(id) ON DELETE CASCADE,
    confirmed_by UUID REFERENCES users(id),
    confirmed_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(price_report_id, confirmed_by)
);

CREATE TABLE price_alerts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    product_id UUID REFERENCES products(id),
    target_price DECIMAL(12,2) NOT NULL,
    radius_km DECIMAL(5,2) DEFAULT 5.0,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE merchant_listings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    merchant_id UUID REFERENCES merchants(id) ON DELETE CASCADE,
    product_id UUID REFERENCES products(id),
    price DECIMAL(12,2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'NGN',
    quantity VARCHAR(50),
    in_stock BOOLEAN DEFAULT TRUE,
    updated_at TIMESTAMP DEFAULT NOW()
);
