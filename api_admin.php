<?php
require 'db.php';

header('Content-Type: application/json');

if (!isset($_SESSION['user_id']) || $_SESSION['user_type'] !== 'admin') {
    echo json_encode(['success' => false, 'message' => 'Unauthorized']);
    exit;
}

$action = $_GET['action'] ?? $_POST['action'] ?? '';

if ($action === 'get_pending_users') {
    $stmt = $pdo->query("SELECT restaurant_id as id, name, email, 'restaurant' as type, created_at as date FROM restaurants WHERE status = 'pending'
                         UNION ALL
                         SELECT receiver_id as id, org_name as name, email, 'receiver' as type, created_at as date FROM receivers WHERE status = 'pending'
                         UNION ALL
                         SELECT volunteer_id as id, (first_name || ' ' || last_name) as name, email, 'volunteer' as type, registered_at as date FROM volunteers WHERE status = 'pending'");
    $users = $stmt->fetchAll();
    echo json_encode(['success' => true, 'data' => $users]);
} elseif ($action === 'approve_user') {
    $id = $_POST['id'] ?? 0;
    $type = $_POST['type'] ?? '';

    $table = '';
    $col = '';
    if ($type === 'restaurant') { $table = 'restaurants'; $col = 'restaurant_id'; }
    elseif ($type === 'receiver') { $table = 'receivers'; $col = 'receiver_id'; }
    elseif ($type === 'volunteer') { $table = 'volunteers'; $col = 'volunteer_id'; }

    if ($table) {
        $stmt = $pdo->prepare("UPDATE $table SET status = 'approved' WHERE $col = ?");
        $stmt->execute([$id]);
        echo json_encode(['success' => true, 'message' => 'User approved successfully.']);
    } else {
        echo json_encode(['success' => false, 'message' => 'Invalid user type.']);
    }
} elseif ($action === 'get_all_donations') {
    $stmt = $pdo->query("SELECT d.*, r.name as restaurant_name FROM donations d JOIN restaurants r ON d.restaurant_id = r.restaurant_id ORDER BY d.created_at DESC");
    $donations = $stmt->fetchAll();
    echo json_encode(['success' => true, 'data' => $donations]);
} elseif ($action === 'get_deliveries') {
    $stmt = $pdo->query("SELECT d.*, don.food_name, r.name as restaurant_name, rec.org_name as receiver_name FROM deliveries d JOIN donations don ON d.donation_id = don.donation_id JOIN restaurants r ON don.restaurant_id = r.restaurant_id JOIN receivers rec ON d.receiver_id = rec.receiver_id ORDER BY d.created_at DESC");
    $deliveries = $stmt->fetchAll();
    echo json_encode(['success' => true, 'data' => $deliveries]);
} else {
    echo json_encode(['success' => false, 'message' => 'Unknown action']);
}
