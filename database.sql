CREATE DATABASE IF NOT EXISTS foodbridge;
USE foodbridge;

-- Admin Table
CREATE TABLE IF NOT EXISTS admins (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'admin',
    last_login DATETIME NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Restaurants Table
CREATE TABLE IF NOT EXISTS restaurants (
    restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    owner_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    fssai_no VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Receivers (Organizations) Table
CREATE TABLE IF NOT EXISTS receivers (
    receiver_id INT AUTO_INCREMENT PRIMARY KEY,
    org_name VARCHAR(100) NOT NULL,
    org_type VARCHAR(50) NOT NULL,
    rep_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    reg_no VARCHAR(50) NOT NULL,
    beneficiaries_count INT DEFAULT 0,
    password_hash VARCHAR(255) NOT NULL,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Volunteers Table
CREATE TABLE IF NOT EXISTS volunteers (
    volunteer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    city VARCHAR(50) NOT NULL,
    aadhar_no VARCHAR(20) NOT NULL,
    vehicle_type VARCHAR(50) NOT NULL,
    availability VARCHAR(50) NOT NULL,
    about TEXT,
    password_hash VARCHAR(255) NOT NULL,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Food Donations Table
CREATE TABLE IF NOT EXISTS donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    food_name VARCHAR(150) NOT NULL,
    quantity INT NOT NULL,
    food_type VARCHAR(50) NOT NULL,
    packaging VARCHAR(50) NOT NULL,
    prep_time DATETIME NOT NULL,
    expiry_time DATETIME NOT NULL,
    pickup_address TEXT NOT NULL,
    pickup_city VARCHAR(50) NOT NULL,
    pickup_phone VARCHAR(20) NOT NULL,
    special_instructions TEXT,
    status ENUM('available', 'requested', 'assigned', 'completed', 'expired') DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id) ON DELETE CASCADE
);

-- Deliveries / Requests Table
CREATE TABLE IF NOT EXISTS deliveries (
    delivery_id INT AUTO_INCREMENT PRIMARY KEY,
    donation_id INT NOT NULL,
    receiver_id INT NOT NULL,
    volunteer_id INT NULL,
    status ENUM('requested', 'assigned', 'picked_up', 'delivered') DEFAULT 'requested',
    pickup_time DATETIME NULL,
    delivered_at DATETIME NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (donation_id) REFERENCES donations(donation_id) ON DELETE CASCADE,
    FOREIGN KEY (receiver_id) REFERENCES receivers(receiver_id) ON DELETE CASCADE,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE SET NULL
);

-- Insert Demo Admin
-- Password is 'admin123'
INSERT IGNORE INTO admins (username, email, password_hash) 
VALUES ('Super Admin', 'admin@foodbridge.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi');
