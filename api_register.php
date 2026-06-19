<?php
require 'db.php';

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['success' => false, 'message' => 'Invalid request method']);
    exit;
}

$action = $_POST['action'] ?? '';

if ($action === 'register_restaurant') {
    $name = $_POST['name'] ?? '';
    $owner_name = $_POST['owner_name'] ?? '';
    $fssai_no = $_POST['fssai_no'] ?? '';
    $email = $_POST['email'] ?? '';
    $phone = $_POST['phone'] ?? '';
    $address = $_POST['address'] ?? '';
    $city = $_POST['city'] ?? '';
    $password = $_POST['password'] ?? '';

    $stmt = $pdo->prepare("SELECT restaurant_id FROM restaurants WHERE email = ?");
    $stmt->execute([$email]);
    if ($stmt->fetch()) {
        echo json_encode(['success' => false, 'message' => 'Email already registered.']);
        exit;
    }

    $hash = password_hash($password, PASSWORD_DEFAULT);
    $stmt = $pdo->prepare("INSERT INTO restaurants (name, owner_name, email, phone, address, city, fssai_no, password_hash, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'approved')");
    if ($stmt->execute([$name, $owner_name, $email, $phone, $address, $city, $fssai_no, $hash])) {
        echo json_encode(['success' => true, 'message' => 'Restaurant registered successfully.']);
    } else {
        echo json_encode(['success' => false, 'message' => 'Registration failed.']);
    }
} elseif ($action === 'register_receiver') {
    $org_name = $_POST['org_name'] ?? '';
    $org_type = $_POST['org_type'] ?? '';
    $reg_no = $_POST['reg_no'] ?? '';
    $rep_name = $_POST['rep_name'] ?? '';
    $email = $_POST['email'] ?? '';
    $phone = $_POST['phone'] ?? '';
    $address = $_POST['address'] ?? '';
    $city = $_POST['city'] ?? '';
    $beneficiaries = $_POST['beneficiaries'] ?? 0;
    $password = $_POST['password'] ?? '';

    $stmt = $pdo->prepare("SELECT receiver_id FROM receivers WHERE email = ?");
    $stmt->execute([$email]);
    if ($stmt->fetch()) {
        echo json_encode(['success' => false, 'message' => 'Email already registered.']);
        exit;
    }

    $hash = password_hash($password, PASSWORD_DEFAULT);
    $stmt = $pdo->prepare("INSERT INTO receivers (org_name, org_type, rep_name, email, phone, address, city, reg_no, beneficiaries_count, password_hash, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'approved')");
    if ($stmt->execute([$org_name, $org_type, $rep_name, $email, $phone, $address, $city, $reg_no, $beneficiaries, $hash])) {
        echo json_encode(['success' => true, 'message' => 'Organization registered successfully.']);
    } else {
        echo json_encode(['success' => false, 'message' => 'Registration failed.']);
    }
} elseif ($action === 'register_volunteer') {
    $first_name = $_POST['first_name'] ?? '';
    $last_name = $_POST['last_name'] ?? '';
    $email = $_POST['email'] ?? '';
    $phone = $_POST['phone'] ?? '';
    $city = $_POST['city'] ?? '';
    $aadhar_no = $_POST['aadhar_no'] ?? '';
    $vehicle_type = $_POST['vehicle_type'] ?? '';
    $availability = $_POST['availability'] ?? '';
    $about = $_POST['about'] ?? '';
    $password = $_POST['password'] ?? '';

    $stmt = $pdo->prepare("SELECT volunteer_id FROM volunteers WHERE email = ?");
    $stmt->execute([$email]);
    if ($stmt->fetch()) {
        echo json_encode(['success' => false, 'message' => 'Email already registered.']);
        exit;
    }

    $hash = password_hash($password, PASSWORD_DEFAULT);
    $stmt = $pdo->prepare("INSERT INTO volunteers (first_name, last_name, email, phone, city, aadhar_no, vehicle_type, availability, about, password_hash, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'approved')");
    if ($stmt->execute([$first_name, $last_name, $email, $phone, $city, $aadhar_no, $vehicle_type, $availability, $about, $hash])) {
        echo json_encode(['success' => true, 'message' => 'Volunteer registered successfully.']);
    } else {
        echo json_encode(['success' => false, 'message' => 'Registration failed.']);
    }
} else {
    echo json_encode(['success' => false, 'message' => 'Unknown action']);
}
