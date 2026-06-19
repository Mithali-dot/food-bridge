import re

def main():
    with open('index.php', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Restaurant Login
    r_login_old = """    <div id="r-login" class="card-form">
      <div class="alert alert-info">ℹ️ Demo: Use any email & password to explore the system</div>
      <div class="form-group"><label>Email Address</label><input type="email" placeholder="restaurant@example.com"></div>
      <div class="form-group"><label>Password</label><input type="password" placeholder="••••••••"></div>
      <button class="btn-submit" onclick="loginSuccess('restaurant')">Login to Dashboard</button>
      <div class="form-switch">Don't have an account? <a onclick="switchTab('r','register')">Register here</a></div>
    </div>"""
    r_login_new = """    <div id="r-login" class="card-form">
      <form onsubmit="event.preventDefault(); doLogin('login_restaurant', this);">
      <div class="form-group"><label>Email Address</label><input type="email" name="email" required placeholder="restaurant@example.com"></div>
      <div class="form-group"><label>Password</label><input type="password" name="password" required placeholder="••••••••"></div>
      <button type="submit" class="btn-submit">Login to Dashboard</button>
      <div class="form-switch">Don't have an account? <a onclick="switchTab('r','register')">Register here</a></div>
      </form>
    </div>"""
    content = content.replace(r_login_old, r_login_new)

    # 2. Restaurant Register
    r_reg_old = """    <div id="r-register" class="card-form" style="display:none">
      <div class="form-group"><label>Restaurant Name</label><input type="text" placeholder="e.g. Spice Garden Restaurant"></div>
      <div class="form-row">
        <div class="form-group"><label>Owner Name</label><input type="text" placeholder="Full name"></div>
        <div class="form-group"><label>FSSAI License No.</label><input type="text" placeholder="FSSAI number"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Email</label><input type="email" placeholder="email@restaurant.com"></div>
        <div class="form-group"><label>Phone</label><input type="tel" placeholder="+91 XXXXX XXXXX"></div>
      </div>
      <div class="form-group"><label>Full Address</label><textarea placeholder="Street address, landmark, city..."></textarea></div>
      <div class="form-row">
        <div class="form-group"><label>City</label><input type="text" placeholder="Your city"></div>
        <div class="form-group"><label>Pincode</label><input type="text" placeholder="560001"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Password</label><input type="password" placeholder="Create password"></div>
        <div class="form-group"><label>Confirm Password</label><input type="password" placeholder="Repeat password"></div>
      </div>
      <button class="btn-submit" onclick="showModal('regModal')">Register Restaurant</button>
      <div class="form-switch">Already registered? <a onclick="switchTab('r','login')">Login here</a></div>
    </div>"""
    r_reg_new = """    <div id="r-register" class="card-form" style="display:none">
      <form onsubmit="event.preventDefault(); doRegister('register_restaurant', this);">
      <div class="form-group"><label>Restaurant Name</label><input type="text" name="name" required placeholder="e.g. Spice Garden Restaurant"></div>
      <div class="form-row">
        <div class="form-group"><label>Owner Name</label><input type="text" name="owner_name" required placeholder="Full name"></div>
        <div class="form-group"><label>FSSAI License No.</label><input type="text" name="fssai_no" required placeholder="FSSAI number"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Email</label><input type="email" name="email" required placeholder="email@restaurant.com"></div>
        <div class="form-group"><label>Phone</label><input type="tel" name="phone" required placeholder="+91 XXXXX XXXXX"></div>
      </div>
      <div class="form-group"><label>Full Address</label><textarea name="address" required placeholder="Street address, landmark, city..."></textarea></div>
      <div class="form-row">
        <div class="form-group"><label>City</label><input type="text" name="city" required placeholder="Your city"></div>
        <div class="form-group"><label>Pincode</label><input type="text" name="pincode" placeholder="560001"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Password</label><input type="password" name="password" required placeholder="Create password"></div>
        <div class="form-group"><label>Confirm Password</label><input type="password" placeholder="Repeat password"></div>
      </div>
      <button type="submit" class="btn-submit">Register Restaurant</button>
      <div class="form-switch">Already registered? <a onclick="switchTab('r','login')">Login here</a></div>
      </form>
    </div>"""
    content = content.replace(r_reg_old, r_reg_new)

    # 3. Receiver Login
    o_login_old = """    <div id="o-login" class="card-form">
      <div class="alert alert-info">ℹ️ Demo: Use any credentials to explore</div>
      <div class="form-group"><label>Email Address</label><input type="email" placeholder="ngo@example.org"></div>
      <div class="form-group"><label>Password</label><input type="password" placeholder="••••••••"></div>
      <button class="btn-submit navy" onclick="loginSuccess('receiver')">Login to Dashboard</button>
      <div class="form-switch">Not registered? <a onclick="switchTab('o','register')">Register your organization</a></div>
    </div>"""
    o_login_new = """    <div id="o-login" class="card-form">
      <form onsubmit="event.preventDefault(); doLogin('login_receiver', this);">
      <div class="form-group"><label>Email Address</label><input type="email" name="email" required placeholder="ngo@example.org"></div>
      <div class="form-group"><label>Password</label><input type="password" name="password" required placeholder="••••••••"></div>
      <button type="submit" class="btn-submit navy">Login to Dashboard</button>
      <div class="form-switch">Not registered? <a onclick="switchTab('o','register')">Register your organization</a></div>
      </form>
    </div>"""
    content = content.replace(o_login_old, o_login_new)

    # 4. Receiver Register
    o_reg_old = """    <div id="o-register" class="card-form" style="display:none">
      <div class="form-group"><label>Organization Name</label><input type="text" placeholder="e.g. Helping Hands NGO"></div>
      <div class="form-row">
        <div class="form-group"><label>Organization Type</label>
          <select><option>NGO</option><option>Orphanage</option><option>Ashram</option><option>Old Age Home</option><option>School / Trust</option></select>
        </div>
        <div class="form-group"><label>Registration No.</label><input type="text" placeholder="Govt reg number"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Representative Name</label><input type="text" placeholder="Full name"></div>
        <div class="form-group"><label>Designation</label><input type="text" placeholder="e.g. Director, Coordinator"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Email</label><input type="email" placeholder="org@ngo.org"></div>
        <div class="form-group"><label>Phone</label><input type="tel" placeholder="+91 XXXXX XXXXX"></div>
      </div>
      <div class="form-group"><label>Address</label><textarea placeholder="Full address of your organization..."></textarea></div>
      <div class="form-row">
        <div class="form-group"><label>City</label><input type="text" placeholder="City"></div>
        <div class="form-group"><label>Beneficiaries Count</label><input type="number" placeholder="e.g. 120"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Password</label><input type="password" placeholder="Create password"></div>
        <div class="form-group"><label>Confirm Password</label><input type="password" placeholder="Repeat password"></div>
      </div>
      <button class="btn-submit navy" onclick="showModal('regModal')">Register Organization</button>
      <div class="form-switch">Already have an account? <a onclick="switchTab('o','login')">Login here</a></div>
    </div>"""
    o_reg_new = """    <div id="o-register" class="card-form" style="display:none">
      <form onsubmit="event.preventDefault(); doRegister('register_receiver', this);">
      <div class="form-group"><label>Organization Name</label><input type="text" name="org_name" required placeholder="e.g. Helping Hands NGO"></div>
      <div class="form-row">
        <div class="form-group"><label>Organization Type</label>
          <select name="org_type"><option>NGO</option><option>Orphanage</option><option>Ashram</option><option>Old Age Home</option><option>School / Trust</option></select>
        </div>
        <div class="form-group"><label>Registration No.</label><input type="text" name="reg_no" required placeholder="Govt reg number"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Representative Name</label><input type="text" name="rep_name" required placeholder="Full name"></div>
        <div class="form-group"><label>Designation</label><input type="text" name="designation" placeholder="e.g. Director, Coordinator"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Email</label><input type="email" name="email" required placeholder="org@ngo.org"></div>
        <div class="form-group"><label>Phone</label><input type="tel" name="phone" required placeholder="+91 XXXXX XXXXX"></div>
      </div>
      <div class="form-group"><label>Address</label><textarea name="address" required placeholder="Full address of your organization..."></textarea></div>
      <div class="form-row">
        <div class="form-group"><label>City</label><input type="text" name="city" required placeholder="City"></div>
        <div class="form-group"><label>Beneficiaries Count</label><input type="number" name="beneficiaries" placeholder="e.g. 120"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Password</label><input type="password" name="password" required placeholder="Create password"></div>
        <div class="form-group"><label>Confirm Password</label><input type="password" placeholder="Repeat password"></div>
      </div>
      <button type="submit" class="btn-submit navy">Register Organization</button>
      <div class="form-switch">Already have an account? <a onclick="switchTab('o','login')">Login here</a></div>
      </form>
    </div>"""
    content = content.replace(o_reg_old, o_reg_new)

    # 5. Volunteer Register
    v_reg_old = """    <div class="card-form">
      <div class="alert alert-success">✅ Volunteers are verified by admin before their first delivery</div>
      <div class="form-row">
        <div class="form-group"><label>First Name</label><input type="text" placeholder="First name"></div>
        <div class="form-group"><label>Last Name</label><input type="text" placeholder="Last name"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Email</label><input type="email" placeholder="your@email.com"></div>
        <div class="form-group"><label>Phone</label><input type="tel" placeholder="+91 XXXXX XXXXX"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>City</label><input type="text" placeholder="City"></div>
        <div class="form-group"><label>Aadhar / ID No.</label><input type="text" placeholder="For verification"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Vehicle Type</label>
          <select><option>Bicycle</option><option>Two-Wheeler</option><option>Car</option><option>Auto Rickshaw</option><option>Walk (Nearby only)</option></select>
        </div>
        <div class="form-group"><label>Availability</label>
          <select><option>Weekdays</option><option>Weekends</option><option>Anytime</option><option>Mornings only</option><option>Evenings only</option></select>
        </div>
      </div>
      <div class="form-group"><label>About Yourself</label><textarea placeholder="Brief note about why you want to volunteer..."></textarea></div>
      <div class="form-row">
        <div class="form-group"><label>Password</label><input type="password" placeholder="Create password"></div>
        <div class="form-group"><label>Confirm Password</label><input type="password" placeholder="Repeat password"></div>
      </div>
      <button class="btn-submit amber">Register as Volunteer</button>
    </div>"""
    v_reg_new = """    <div class="card-form">
      <form onsubmit="event.preventDefault(); doRegister('register_volunteer', this);">
      <div class="alert alert-success">✅ Volunteers are verified by admin before their first delivery</div>
      <div class="form-row">
        <div class="form-group"><label>First Name</label><input type="text" name="first_name" required placeholder="First name"></div>
        <div class="form-group"><label>Last Name</label><input type="text" name="last_name" required placeholder="Last name"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Email</label><input type="email" name="email" required placeholder="your@email.com"></div>
        <div class="form-group"><label>Phone</label><input type="tel" name="phone" required placeholder="+91 XXXXX XXXXX"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>City</label><input type="text" name="city" required placeholder="City"></div>
        <div class="form-group"><label>Aadhar / ID No.</label><input type="text" name="aadhar_no" required placeholder="For verification"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Vehicle Type</label>
          <select name="vehicle_type"><option>Bicycle</option><option>Two-Wheeler</option><option>Car</option><option>Auto Rickshaw</option><option>Walk (Nearby only)</option></select>
        </div>
        <div class="form-group"><label>Availability</label>
          <select name="availability"><option>Weekdays</option><option>Weekends</option><option>Anytime</option><option>Mornings only</option><option>Evenings only</option></select>
        </div>
      </div>
      <div class="form-group"><label>About Yourself</label><textarea name="about" placeholder="Brief note about why you want to volunteer..."></textarea></div>
      <div class="form-row">
        <div class="form-group"><label>Password</label><input type="password" name="password" required placeholder="Create password"></div>
        <div class="form-group"><label>Confirm Password</label><input type="password" placeholder="Repeat password"></div>
      </div>
      <button type="submit" class="btn-submit amber">Register as Volunteer</button>
      </form>
    </div>"""
    content = content.replace(v_reg_old, v_reg_new)

    # 6. Donation Form
    don_old = """    <div class="card-form">
      <div class="alert alert-warn">⏰ Only list food that is safe to consume and within expiry time</div>
      <div class="form-row">
        <div class="form-group"><label>Food Name / Description</label><input type="text" placeholder="e.g. Biryani, Dal Rice, Chapati"></div>
        <div class="form-group"><label>Quantity (Servings)</label><input type="number" placeholder="e.g. 50"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Food Type</label>
          <select><option>Vegetarian</option><option>Non-Vegetarian</option><option>Vegan</option><option>Jain</option></select>
        </div>
        <div class="form-group"><label>Packaging</label>
          <select><option>Packed in containers</option><option>Loose / Bulk</option><option>Sealed packets</option></select>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Preparation Time</label><input type="datetime-local"></div>
        <div class="form-group"><label>Safe Until (Expiry)</label><input type="datetime-local"></div>
      </div>
      <div class="form-group"><label>Pickup Address</label><textarea placeholder="Specific address for food pickup (may differ from restaurant address)..." style="min-height:70px"></textarea></div>
      <div class="form-row">
        <div class="form-group"><label>City</label><input type="text" placeholder="City"></div>
        <div class="form-group"><label>Pickup Contact Number</label><input type="tel" placeholder="+91 XXXXX XXXXX"></div>
      </div>
      <div class="form-group"><label>Special Instructions</label><textarea placeholder="Allergies, temperature notes, handling instructions..." style="min-height:70px"></textarea></div>
      <div class="form-group"><label>Food Image (Optional)</label><input type="file" accept="image/*" style="padding:8px 14px;background:white"></div>
      <button class="btn-submit" onclick="showPage('dashboard')">Post Food Donation</button>
    </div>"""
    don_new = """    <div class="card-form">
      <form onsubmit="event.preventDefault(); doPostDonation(this);">
      <div class="alert alert-warn">⏰ Only list food that is safe to consume and within expiry time</div>
      <div class="form-row">
        <div class="form-group"><label>Food Name / Description</label><input type="text" name="food_name" required placeholder="e.g. Biryani, Dal Rice, Chapati"></div>
        <div class="form-group"><label>Quantity (Servings)</label><input type="number" name="quantity" required placeholder="e.g. 50"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Food Type</label>
          <select name="food_type"><option>Vegetarian</option><option>Non-Vegetarian</option><option>Vegan</option><option>Jain</option></select>
        </div>
        <div class="form-group"><label>Packaging</label>
          <select name="packaging"><option>Packed in containers</option><option>Loose / Bulk</option><option>Sealed packets</option></select>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Preparation Time</label><input type="datetime-local" name="prep_time" required></div>
        <div class="form-group"><label>Safe Until (Expiry)</label><input type="datetime-local" name="expiry_time" required></div>
      </div>
      <div class="form-group"><label>Pickup Address</label><textarea name="pickup_address" required placeholder="Specific address for food pickup..." style="min-height:70px"></textarea></div>
      <div class="form-row">
        <div class="form-group"><label>City</label><input type="text" name="city" required placeholder="City"></div>
        <div class="form-group"><label>Pickup Contact Number</label><input type="tel" name="pickup_phone" required placeholder="+91 XXXXX XXXXX"></div>
      </div>
      <div class="form-group"><label>Special Instructions</label><textarea name="special_instructions" placeholder="Allergies, temperature notes..." style="min-height:70px"></textarea></div>
      <button type="submit" class="btn-submit">Post Food Donation</button>
      </form>
    </div>"""
    content = content.replace(don_old, don_new)

    # 7. Request Form
    req_old = """    <div class="card-form">
      <div id="requestFoodInfo" style="background:var(--green-pale);border-radius:10px;padding:14px 16px;margin-bottom:18px">
        <strong style="color:var(--green);font-size:14px">Selected Food</strong>
        <div id="requestFoodDetails" style="font-size:13px;color:var(--text-muted);margin-top:4px"></div>
      </div>
      <div class="form-group"><label>Organization Name</label><input type="text" placeholder="Your registered org name"></div>
      <div class="form-group"><label>Representative Name</label><input type="text" placeholder="Authorized representative"></div>
      <div class="form-row">
        <div class="form-group"><label>Contact Number</label><input type="tel" placeholder="Phone"></div>
        <div class="form-group"><label>No. of Beneficiaries</label><input type="number" placeholder="People to serve"></div>
      </div>
      <div class="form-group"><label>Pickup / Delivery Preference</label>
        <select><option>Self Pickup</option><option>Volunteer Delivery Needed</option></select>
      </div>
      <div class="form-group"><label>Delivery Address</label><textarea placeholder="Where should the food be delivered?"></textarea></div>
      <div class="form-group"><label>Additional Notes</label><textarea placeholder="Special requirements, dietary restrictions, urgency..."></textarea></div>
      <button class="btn-submit navy" onclick="showModal('requestModal')">Submit Request</button>
    </div>"""
    req_new = """    <div class="card-form">
      <form onsubmit="event.preventDefault(); doRequestFood(this);">
      <input type="hidden" id="reqDonationId" name="donation_id">
      <div id="requestFoodInfo" style="background:var(--green-pale);border-radius:10px;padding:14px 16px;margin-bottom:18px">
        <strong style="color:var(--green);font-size:14px">Selected Food</strong>
        <div id="requestFoodDetails" style="font-size:13px;color:var(--text-muted);margin-top:4px"></div>
      </div>
      <div class="form-group"><label>Organization Name</label><input type="text" required placeholder="Your registered org name"></div>
      <div class="form-group"><label>Representative Name</label><input type="text" required placeholder="Authorized representative"></div>
      <div class="form-row">
        <div class="form-group"><label>Contact Number</label><input type="tel" required placeholder="Phone"></div>
        <div class="form-group"><label>No. of Beneficiaries</label><input type="number" required placeholder="People to serve"></div>
      </div>
      <div class="form-group"><label>Pickup / Delivery Preference</label>
        <select><option>Self Pickup</option><option>Volunteer Delivery Needed</option></select>
      </div>
      <div class="form-group"><label>Delivery Address</label><textarea required placeholder="Where should the food be delivered?"></textarea></div>
      <div class="form-group"><label>Additional Notes</label><textarea placeholder="Special requirements, dietary restrictions, urgency..."></textarea></div>
      <button type="submit" class="btn-submit navy">Submit Request</button>
      </form>
    </div>"""
    content = content.replace(req_old, req_new)

    # 8. Admin login
    admin_old = """    <div class="card-form">
      <div class="alert alert-warn">⚠️ Demo: Use admin / admin123 to access dashboard</div>
      <div class="form-group"><label>Username</label><input type="text" placeholder="admin" id="adminUser"></div>
      <div class="form-group"><label>Password</label><input type="password" placeholder="••••••••" id="adminPass"></div>
      <button class="btn-submit" style="background:var(--coral)" onclick="adminLogin()">Login to Admin Panel</button>
    </div>"""
    admin_new = """    <div class="card-form">
      <form onsubmit="event.preventDefault(); doAdminLogin(this);">
      <div class="alert alert-warn">⚠️ Demo: Use admin@foodbridge.com / admin123</div>
      <div class="form-group"><label>Email</label><input type="email" name="email" required placeholder="admin@foodbridge.com" id="adminUser"></div>
      <div class="form-group"><label>Password</label><input type="password" name="password" required placeholder="••••••••" id="adminPass"></div>
      <button type="submit" class="btn-submit" style="background:var(--coral)">Login to Admin Panel</button>
      </form>
    </div>"""
    content = content.replace(admin_old, admin_new)

    # 9. Replace Javascript
    # We will remove the large chunk of hardcoded JS and inject our dynamic JS
    start_str = "// ─── DATA ───"
    end_str = "</body>"
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    dynamic_js = """
// ─── DYNAMIC JS ───

// Utility
async function fetchPost(url, data) {
    const formData = new FormData();
    for (let key in data) formData.append(key, data[key]);
    const res = await fetch(url, { method: 'POST', body: formData });
    return await res.json();
}

async function doLogin(action, form) {
    const data = { action };
    new FormData(form).forEach((value, key) => data[key] = value);
    const res = await fetchPost('api_login.php', data);
    if (res.success) {
        if (res.user_type === 'restaurant') showPage('donate');
        else showPage('dashboard');
    } else {
        alert(res.message);
    }
}

async function doRegister(action, form) {
    const data = { action };
    new FormData(form).forEach((value, key) => data[key] = value);
    const res = await fetchPost('api_register.php', data);
    if (res.success) {
        showModal('regModal');
        form.reset();
    } else {
        alert(res.message);
    }
}

async function doAdminLogin(form) {
    const data = { action: 'login_admin' };
    new FormData(form).forEach((value, key) => data[key] = value);
    const res = await fetchPost('api_login.php', data);
    if (res.success) {
        showPage('admin');
        renderAdminOverview();
    } else {
        alert(res.message);
    }
}

async function doPostDonation(form) {
    const data = { action: 'add_donation' };
    new FormData(form).forEach((value, key) => data[key] = value);
    const res = await fetchPost('api_donations.php', data);
    if (res.success) {
        form.reset();
        showPage('dashboard');
    } else {
        alert(res.message);
    }
}

async function doRequestFood(form) {
    const data = { action: 'request_food', donation_id: document.getElementById('reqDonationId').value };
    const res = await fetchPost('api_requests.php', data);
    if (res.success) {
        form.reset();
        showModal('requestModal');
    } else {
        alert(res.message);
    }
}

// ─── NAVIGATION ───
function showPage(page) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
  const el = document.getElementById('page-' + page);
  if (el) el.classList.add('active');
  const navEl = document.getElementById('nav-' + page);
  if (navEl) navEl.classList.add('active');
  window.scrollTo(0,0);
  document.getElementById('navLinks').classList.remove('open');
  if (page === 'dashboard') loadDonations();
  if (page === 'admin') { renderAdminOverview(); }
}

function toggleMenu() {
  document.getElementById('navLinks').classList.toggle('open');
}

function switchTab(prefix, tab) {
  document.querySelectorAll(`#${prefix}-login, #${prefix}-register`).forEach(el => el.style.display = 'none');
  document.getElementById(`${prefix}-${tab}`).style.display = 'block';
  document.querySelectorAll('.tab').forEach((t,i) => {
    t.classList.toggle('active', (tab === 'login' && i === 0) || (tab === 'register' && i === 1));
  });
}

// ─── FOODS ───
let allDonations = [];
async function loadDonations() {
    const res = await fetch('api_donations.php', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: 'action=get_donations'
    });
    const json = await res.json();
    if (json.success) {
        allDonations = json.data;
        renderFoods(allDonations);
    }
}

function renderFoods(data) {
  const grid = document.getElementById('foodGrid');
  if (!data.length) { grid.innerHTML = '<div class="empty-state"><div class="icon">🍽️</div><p>No food listings match your search.</p></div>'; return; }
  grid.innerHTML = data.map(f => {
    const statusBadge = f.status === 'available'
      ? '<span class="badge badge-green">● Available</span>'
      : f.status === 'requested' ? '<span class="badge badge-amber">⏳ Requested</span>'
      : '<span class="badge badge-navy">🚴 En Route</span>';
    const typeBadge = f.food_type === 'Vegetarian' || f.food_type === 'Vegan' || f.food_type === 'Jain'
      ? '<span class="badge" style="background:#D8F3DC;color:#1A5C38;font-size:11px">🟢 Veg</span>'
      : '<span class="badge" style="background:var(--coral-pale);color:#8B3820;font-size:11px">🔴 Non-Veg</span>';
    return `<div class="food-card">
      <div class="food-img"><div class="food-tag">${statusBadge}</div><span>🍛</span></div>
      <div class="food-body">
        <h4>${f.food_name}</h4>
        <div class="food-meta">
          <span>${typeBadge}</span>
          <span style="margin-top:4px;display:block;font-size:12px">📍 ${f.pickup_city} &nbsp;|&nbsp; ⏰ Safe till ${new Date(f.expiry_time).toLocaleTimeString()}</span>
          <span style="font-size:12px">🍽️ ${f.quantity} servings</span>
        </div>
        <div class="food-footer">
          <div class="restaurant">🏪 ${f.restaurant_name}</div>
          ${f.status === 'available'
            ? `<button class="btn-sm btn-green" onclick="requestFood(${f.donation_id},'${f.food_name}','${f.restaurant_name}',${f.quantity})">Request</button>`
            : `<button class="btn-sm btn-outline-sm" onclick="showPage('tracking')">Track</button>`}
        </div>
      </div>
    </div>`;
  }).join('');
}

function filterFoods() {
  const q = document.getElementById('foodSearch').value.toLowerCase();
  const type = document.getElementById('typeFilter').value;
  const city = document.getElementById('cityFilter').value;
  const filtered = allDonations.filter(f =>
    (!q || f.food_name.toLowerCase().includes(q) || f.restaurant_name.toLowerCase().includes(q)) &&
    (!type || f.food_type === type) &&
    (!city || f.pickup_city === city)
  );
  renderFoods(filtered);
}

function requestFood(id, name, rest, qty) {
  document.getElementById('reqDonationId').value = id;
  document.getElementById('requestFoodTitle').textContent = `Request: ${name}`;
  document.getElementById('requestFoodDetails').textContent = `${qty} servings from ${rest}`;
  showPage('request');
}

// ─── TRACKING ───
async function showTracking() {
  const trackId = document.getElementById('trackInput').value;
  const res = await fetch(`api_tracking.php?action=track_delivery&tracking_id=${trackId}`);
  const json = await res.json();
  const resultDiv = document.getElementById('trackingResult');
  
  if (json.success) {
      const d = json.data;
      resultDiv.innerHTML = `
      <div class="tracking-card">
        <div class="tracking-top">
          <h3>🍛 ${d.food_name} — ${d.quantity} Servings</h3>
          <p>Donation ID: FB-2024-${d.donation_id} &nbsp;|&nbsp; ${d.restaurant_name} → ${d.receiver_name}</p>
        </div>
        <div class="tracking-body">
          <div style="display:flex;gap:16px;margin-bottom:24px;flex-wrap:wrap">
            <div><div style="font-size:12px;color:var(--text-muted)">Volunteer</div><div style="font-weight:600;font-size:14px">${d.vol_first ? d.vol_first + ' ' + d.vol_last : 'Pending'}</div></div>
            <div><div style="font-size:12px;color:var(--text-muted)">Vehicle</div><div style="font-weight:600;font-size:14px">${d.vehicle_type || 'Pending'}</div></div>
            <div><span class="badge badge-amber">🚴 ${d.status.toUpperCase()}</span></div>
          </div>
        </div>
      </div>`;
      resultDiv.style.display = 'block';
  } else {
      alert(json.message);
  }
}

// ─── ADMIN ───
async function renderAdminOverview() {
  const res = await fetch('api_admin.php?action=get_pending_users');
  const json = await res.json();
  const pending = json.success ? json.data : [];
  
  document.getElementById('adminContent').innerHTML = `
    <h2 style="font-family:var(--font-display);font-size:24px;color:var(--navy);margin-bottom:20px">📊 Admin Overview</h2>
    <div style="display:grid;grid-template-columns:1fr;gap:20px;margin-top:4px">
      <div class="table-wrap">
        <div class="table-head"><h3>⏳ Pending Approvals</h3></div>
        <table>
          <thead><tr><th>Name</th><th>Email</th><th>Type</th><th>Action</th></tr></thead>
          <tbody>
            ${pending.map(p => `<tr><td>${p.name}</td><td>${p.email}</td><td><span class="badge badge-amber">${p.type}</span></td><td><button class="btn-sm btn-green" onclick="approveEntity(${p.id}, '${p.type}', '${p.name}')">Approve</button></td></tr>`).join('') || '<tr><td colspan="4">No pending approvals</td></tr>'}
          </tbody>
        </table>
      </div>
    </div>`;
}

async function approveEntity(id, type, name) {
    const res = await fetchPost('api_admin.php', { action: 'approve_user', id, type });
    if (res.success) {
        document.getElementById('approveMsg').textContent = `${name} has been approved.`;
        showModal('approveModal');
        renderAdminOverview();
    } else {
        alert(res.message);
    }
}

function showAdminTab(tab) {
  document.querySelectorAll('.sidebar-link').forEach(l => l.classList.remove('active'));
  event.currentTarget.classList.add('active');
  if (tab === 'overview') renderAdminOverview();
  else if (tab === 'donations') renderAdminDonations();
}

async function renderAdminDonations() {
  const res = await fetch('api_admin.php?action=get_all_donations');
  const json = await res.json();
  const donations = json.success ? json.data : [];
  document.getElementById('adminContent').innerHTML = `
    <h2 style="font-family:var(--font-display);font-size:24px;color:var(--navy);margin-bottom:20px">🍛 Donations</h2>
      <div class="table-wrap">
        <div class="table-head"><h3>All Food Donations</h3></div>
        <table><thead><tr><th>ID</th><th>Food</th><th>Qty</th><th>Restaurant</th><th>Status</th></tr></thead>
        <tbody>${donations.map(d => `
          <tr><td>${d.donation_id}</td><td>${d.food_name}</td><td>${d.quantity}</td><td>${d.restaurant_name}</td>
          <td><span class="badge badge-gray">${d.status}</span></td></tr>
        `).join('')}</tbody></table>
      </div>`;
}

// ─── MODALS ───
function showModal(id) { document.getElementById(id).classList.add('open'); }
function closeModal(id) { document.getElementById(id).classList.remove('open'); }
document.querySelectorAll('.modal-overlay').forEach(m => {
  m.addEventListener('click', e => { if (e.target === m) m.classList.remove('open'); });
});

loadDonations();
</script>
"""
    
    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + dynamic_js + content[end_idx:]
        
    with open('index.php', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
