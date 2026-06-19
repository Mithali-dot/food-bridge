<?php
require 'db.php';

header('Content-Type: application/json');

$action = $_GET['action'] ?? $_POST['action'] ?? '';

if ($action === 'track_delivery') {
    $tracking_id = $_GET['tracking_id'] ?? '';
    
    // We expect tracking ID like FB-2024-XXX where XXX is donation_id
    $parts = explode('-', $tracking_id);
    $donation_id = end($parts);
    
    if (!is_numeric($donation_id)) {
        echo json_encode(['success' => false, 'message' => 'Invalid Tracking ID format.']);
        exit;
    }

    $stmt = $pdo->prepare("
        SELECT d.*, 
               don.food_name, don.quantity, 
               r.name as restaurant_name, 
               rec.org_name as receiver_name,
               v.first_name as vol_first, v.last_name as vol_last, v.vehicle_type
        FROM deliveries d
        JOIN donations don ON d.donation_id = don.donation_id
        JOIN restaurants r ON don.restaurant_id = r.restaurant_id
        JOIN receivers rec ON d.receiver_id = rec.receiver_id
        LEFT JOIN volunteers v ON d.volunteer_id = v.volunteer_id
        WHERE d.donation_id = ?
    ");
    $stmt->execute([$donation_id]);
    $delivery = $stmt->fetch();

    if ($delivery) {
        echo json_encode(['success' => true, 'data' => $delivery]);
    } else {
        echo json_encode(['success' => false, 'message' => 'No delivery found for this Tracking ID.']);
    }
} else {
    echo json_encode(['success' => false, 'message' => 'Unknown action']);
}
