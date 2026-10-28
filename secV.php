Procedure
Step 1: Make a folder inside xampp inside htdocs

Bash
mkdir /p5
cd p5
Step 2: Create the filelogin.php

Step 3: Write the code

PHP
<?php 
session_start(); 
if ($_SERVER['REQUEST_METHOD'] == 'POST') { 
    $_SESSION['user'] = 'alice'; 
} 
echo "Session ID: " . session_id(); 
Step 4: Save the file
Press Ctrl+O, Enter, and then Ctrl+X.

Step 5: Open in your browser
Go to: http://localhost:8000/login.php

Step 6: Inspect the cookies
Press F12 → go to the Application tab → Cookies → click localhost. Notice that the cookie has no checkmarks under Secure, HttpOnly, or SameSite — this is the insecure version.

Step 7: Update the code for security
Go back to your terminal (press Ctrl+C to stop the server) and edit the file again (nano login.php). Change the code to include cookie parameters before starting the session:

PHP
<?php 
session_set_cookie_params([
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Strict'
]); 
session_start(); 

if ($_SERVER['REQUEST_METHOD'] == 'POST') { 
    $_SESSION['user'] = 'alice'; 
} 
echo "Session ID: " . session_id(); 
Step 8: Verify the changes
Save the file, run php -S localhost:8000 again, refresh your browser, and check the cookies tab again. You should now see the security flags applied.