<?php
require 'db.php';

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['success' => false, 'message' => 'Invalid request method']);
    exit;
}

$action = $_POST['action'] ?? '';
$email = $_POST['email'] ?? '';
$password = $_POST['password'] ?? '';

if ($action === 'login_restaurant') {
    $stmt = $pdo->prepare("SELECT * FROM restaurants WHERE email = ?");
    $stmt->execute([$email]);
    $user = $stmt->fetch();

    if ($user && password_verify($password, $user['password_hash'])) {
        if ($user['status'] === 'rejected') {
            echo json_encode(['success' => false, 'message' => 'Your account has been rejected.']);
            exit;
        }
        $_SESSION['user_id'] = $user['restaurant_id'];
        $_SESSION['user_type'] = 'restaurant';
        $_SESSION['user_name'] = $user['name'];
        echo json_encode(['success' => true, 'user_type' => 'restaurant']);
    } else {
        echo json_encode(['success' => false, 'message' => 'Invalid credentials']);
    }
} elseif ($action === 'login_receiver') {
    $stmt = $pdo->prepare("SELECT * FROM receivers WHERE email = ?");
    $stmt->execute([$email]);
    $user = $stmt->fetch();

    if ($user && password_verify($password, $user['password_hash'])) {
        if ($user['status'] === 'rejected') {
            echo json_encode(['success' => false, 'message' => 'Your account has been rejected.']);
            exit;
        }
        $_SESSION['user_id'] = $user['receiver_id'];
        $_SESSION['user_type'] = 'receiver';
        $_SESSION['user_name'] = $user['org_name'];
        echo json_encode(['success' => true, 'user_type' => 'receiver']);
    } else {
        echo json_encode(['success' => false, 'message' => 'Invalid credentials']);
    }
} elseif ($action === 'login_volunteer') {
    $stmt = $pdo->prepare("SELECT * FROM volunteers WHERE email = ?");
    $stmt->execute([$email]);
    $user = $stmt->fetch();

    if ($user && password_verify($password, $user['password_hash'])) {
        if ($user['status'] === 'rejected') {
            echo json_encode(['success' => false, 'message' => 'Your account has been rejected.']);
            exit;
        }
        $_SESSION['user_id'] = $user['volunteer_id'];
        $_SESSION['user_type'] = 'volunteer';
        $_SESSION['user_name'] = $user['first_name'] . ' ' . $user['last_name'];
        echo json_encode(['success' => true, 'user_type' => 'volunteer']);
    } else {
        echo json_encode(['success' => false, 'message' => 'Invalid credentials']);
    }
} elseif ($action === 'login_admin') {
    $stmt = $pdo->prepare("SELECT * FROM admins WHERE email = ?");
    $stmt->execute([$email]);
    $user = $stmt->fetch();

    if ($user && password_verify($password, $user['password_hash'])) {
        $_SESSION['user_id'] = $user['admin_id'];
        $_SESSION['user_type'] = 'admin';
        $_SESSION['user_name'] = $user['username'];
        $pdo->prepare("UPDATE admins SET last_login = datetime('now', 'localtime') WHERE admin_id = ?")->execute([$user['admin_id']]);
        echo json_encode(['success' => true, 'user_type' => 'admin']);
    } else {
        echo json_encode(['success' => false, 'message' => 'Invalid admin credentials']);
    }
} elseif ($action === 'logout') {
    session_destroy();
    echo json_encode(['success' => true]);
} elseif ($action === 'check_session') {
    if (isset($_SESSION['user_id'])) {
        echo json_encode(['success' => true, 'user_type' => $_SESSION['user_type'], 'user_name' => $_SESSION['user_name']]);
    } else {
        echo json_encode(['success' => false]);
    }
} else {
    echo json_encode(['success' => false, 'message' => 'Unknown action']);
}
