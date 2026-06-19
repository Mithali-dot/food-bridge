<?php
require 'db.php';

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['success' => false, 'message' => 'Invalid request method']);
    exit;
}

$action = $_POST['action'] ?? '';

if ($action === 'request_food') {
    if (!isset($_SESSION['user_id']) || $_SESSION['user_type'] !== 'receiver') {
        echo json_encode(['success' => false, 'message' => 'Unauthorized']);
        exit;
    }

    $donation_id = $_POST['donation_id'] ?? 0;
    $receiver_id = $_SESSION['user_id'];

    // Verify donation is still available
    $stmt = $pdo->prepare("SELECT status FROM donations WHERE donation_id = ?");
    $stmt->execute([$donation_id]);
    $donation = $stmt->fetch();

    if (!$donation || $donation['status'] !== 'available') {
        echo json_encode(['success' => false, 'message' => 'This food donation is no longer available.']);
        exit;
    }

    $pdo->beginTransaction();
    try {
        // Update donation status
        $stmt = $pdo->prepare("UPDATE donations SET status = 'requested' WHERE donation_id = ?");
        $stmt->execute([$donation_id]);

        // Create delivery request
        $stmt = $pdo->prepare("INSERT INTO deliveries (donation_id, receiver_id, status) VALUES (?, ?, 'requested')");
        $stmt->execute([$donation_id, $receiver_id]);

        $pdo->commit();
        echo json_encode(['success' => true, 'message' => 'Food requested successfully!']);
    } catch (Exception $e) {
        $pdo->rollBack();
        echo json_encode(['success' => false, 'message' => 'Failed to process request: ' . $e->getMessage()]);
    }
} else {
    echo json_encode(['success' => false, 'message' => 'Unknown action']);
}
