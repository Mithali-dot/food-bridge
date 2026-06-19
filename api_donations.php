<?php
require 'db.php';

header('Content-Type: application/json');

$action = $_POST['action'] ?? ($_GET['action'] ?? '');

if ($action === 'add_donation') {
    if (!isset($_SESSION['user_id']) || $_SESSION['user_type'] !== 'restaurant') {
        echo json_encode(['success' => false, 'message' => 'Unauthorized']);
        exit;
    }

    $food_name = $_POST['food_name'] ?? '';
    $quantity = $_POST['quantity'] ?? 0;
    $food_type = $_POST['food_type'] ?? '';
    $packaging = $_POST['packaging'] ?? '';
    $prep_time = $_POST['prep_time'] ?? '';
    $expiry_time = $_POST['expiry_time'] ?? '';
    $pickup_address = $_POST['pickup_address'] ?? '';
    $city = $_POST['city'] ?? '';
    $pickup_phone = $_POST['pickup_phone'] ?? '';
    $special_instructions = $_POST['special_instructions'] ?? '';
    $restaurant_id = $_SESSION['user_id'];

    $stmt = $pdo->prepare("INSERT INTO donations (restaurant_id, food_name, quantity, food_type, packaging, prep_time, expiry_time, pickup_address, pickup_city, pickup_phone, special_instructions) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
    if ($stmt->execute([$restaurant_id, $food_name, $quantity, $food_type, $packaging, $prep_time, $expiry_time, $pickup_address, $city, $pickup_phone, $special_instructions])) {
        $donation_id = $pdo->lastInsertId();
        echo json_encode(['success' => true, 'message' => 'Donation posted successfully', 'donation_id' => $donation_id]);
    } else {
        echo json_encode(['success' => false, 'message' => 'Failed to post donation']);
    }
} elseif ($action === 'get_donations') {
    // Get active donations for dashboard
    $stmt = $pdo->prepare("
        SELECT d.*, r.name as restaurant_name 
        FROM donations d
        JOIN restaurants r ON d.restaurant_id = r.restaurant_id
        WHERE d.status = 'available' AND datetime(d.expiry_time) > datetime('now', 'localtime')
        ORDER BY d.created_at DESC
    ");
    $stmt->execute();
    $donations = $stmt->fetchAll();
    echo json_encode(['success' => true, 'data' => $donations]);
} elseif ($action === 'get_stats') {
    // Get dashboard stats
    $stmt = $pdo->query("SELECT COUNT(*) as active FROM donations WHERE status = 'available' AND datetime(expiry_time) > datetime('now', 'localtime')");
    $active = $stmt->fetch()['active'];

    $stmt = $pdo->query("SELECT COUNT(*) as requested FROM deliveries WHERE status = 'requested'");
    $requested = $stmt->fetch()['requested'];

    $stmt = $pdo->query("SELECT COUNT(*) as completed FROM deliveries WHERE status = 'delivered' AND date(delivered_at) = date('now')");
    $completed = $stmt->fetch()['completed'];

    $stmt = $pdo->query("SELECT COUNT(*) as enroute FROM deliveries WHERE status = 'picked_up'");
    $enroute = $stmt->fetch()['enroute'];

    echo json_encode(['success' => true, 'stats' => [
        'active' => $active,
        'requested' => $requested,
        'completed' => $completed,
        'enroute' => $enroute
    ]]);
} elseif ($action === 'get_home_stats') {
    $meals = $pdo->query("SELECT SUM(quantity) as count FROM donations")->fetch()['count'] ?? 0;
    $rests = $pdo->query("SELECT COUNT(*) as count FROM restaurants")->fetch()['count'];
    $orgs = $pdo->query("SELECT COUNT(*) as count FROM receivers")->fetch()['count'];
    $vols = $pdo->query("SELECT COUNT(*) as count FROM volunteers")->fetch()['count'];
    echo json_encode(['success' => true, 'stats' => [
        'meals' => $meals, 
        'rests' => $rests, 
        'orgs' => $orgs, 
        'vols' => $vols
    ]]);
} else {
    echo json_encode(['success' => false, 'message' => 'Unknown action']);
}
