# Beginner Explanatory Guide: DEVTOOLS-101: Resolve Merge Conflicts in User Auth Module

> **Task Type**: Service Task  
> **Domain/Focus**: Python Fundamentals, Git Version Control

---

## 1. The Goal (In-Depth Beginner Explanation)

### The Core Problem
In software development, multiple developers often work on the same codebase simultaneously. This can lead to situations where two developers make changes to the same file, resulting in what is known as a "merge conflict." In this task, two developers, Priya and Arjun, have both modified the `authService.py` file, which is responsible for user authentication and token management. Arjun's changes were merged first, and now Priya's branch has conflicts that need to be resolved.

The current state of the `authService.py` file contains conflict markers (like `<<<<<<<`, `=======`, and `>>>>>>>`) that indicate where the conflicting changes are. These markers disrupt the functionality of the code, making it impossible for the application to run correctly. Resolving these conflicts is crucial because it ensures that both developers' contributions are preserved, allowing the application to function as intended while incorporating the latest features and improvements.

### Jargon Buster (Key Terms Explained)
* **Merge Conflict**: A situation that occurs in version control systems (like Git) when two branches have changes to the same line of a file, and Git cannot automatically determine which change to keep. For example, if Developer A changes a function's logic and Developer B changes the same function's return value, merging their branches will create a conflict.

* **Conflict Markers**: Special strings inserted by Git in files that have merge conflicts. They indicate the conflicting sections of code. For instance, `<<<<<<< HEAD` shows the code from the current branch, while `>>>>>>> feature/branch-name` shows the code from the branch being merged.

* **Bcrypt**: A password hashing function designed to be computationally intensive to make brute-force attacks more difficult. It adds a random salt to the password before hashing, which helps protect against rainbow table attacks. For example, hashing the password "mypassword" with bcrypt will produce a different hash each time due to the salt.

* **JWT (JSON Web Token)**: A compact, URL-safe means of representing claims to be transferred between two parties. The claims in a JWT are encoded as a JSON object that is used as the payload of a JSON Web Signature (JWS) structure or as the plaintext of a JSON Web Encryption (JWE) structure. For example, a JWT can be used to securely transmit user information between a client and a server.

### Expected Outcome
After resolving the merge conflicts, the `authService.py` file should function correctly without any conflict markers. The expected changes include:
- The `validate_token()` method from Priya's branch should be present and operational.
- The `hash_password()` method should utilize bcrypt as implemented by Arjun.
- All relevant import statements from both branches should be included.
- The code should be free of any conflict markers, ensuring it is clean and ready for deployment.

**Before vs. After**:
- **Before**: The file contains conflict markers, and the application cannot run due to unresolved conflicts.
- **After**: The file is clean, with both developers' changes integrated, allowing the application to function correctly and securely.

---

## 2. Related Coding Concepts & Syntax (50% Theory, 50% Practice)

### Concept 1: Git Merge Conflicts
#### 📘 Theoretical Overview (50%)
Git is a version control system that helps developers manage changes to their code. When multiple developers work on the same file, Git tries to merge their changes automatically. However, if two developers modify the same line or nearby lines, Git cannot decide which change to keep, resulting in a merge conflict. This is a critical situation that needs to be resolved manually to ensure that all intended changes are preserved.

If merge conflicts are not resolved, the code will not compile or run correctly, leading to potential bugs and issues in the application. Understanding how to resolve these conflicts is essential for collaborative software development, as it ensures that all contributions are integrated smoothly.

#### 💻 Syntax & Practical Examples (50%)
* **Language Syntax**:
  ```bash
  git merge feature/branch-name
  # If a conflict occurs, Git will output conflict markers in the affected files.
  ```

* **Real-World Application**:
  ```bash
  # Assume you are on the main branch and want to merge a feature branch.
  git checkout main
  git merge feature/token-validation
  # If conflicts arise, open the conflicting file and look for conflict markers.
  # Resolve the conflicts by editing the file, then:
  git add authService.py
  git commit -m "Resolved merge conflicts in authService.py"
  ```

---

## 3. Step-by-Step Logic & Walkthrough

1. **Step 1: Locate and Analyze the Target File**
   * Navigate to the `src` folder within the `s-w09-task-03` directory.
   * Open the `authService.py` file, which contains the merge conflict markers.

2. **Step 2: Input Verification & Validation**
   * Check the file for the presence of conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
   * Identify the sections of code that need to be merged from both branches.

3. **Step 3: Core Implementation / Modification**
   * Carefully read through the conflicting sections:
     - Keep Priya's `validate_token()` method.
     - Replace Arjun's `hash_password()` method with the bcrypt implementation.
     - Combine the import statements from both branches.
   * Remove all conflict markers after resolving the conflicts.

4. **Step 4: Output Verification & Testing**
   * Save the changes to `authService.py`.
   * Run the test suite using `pytest` to ensure all tests pass and the application behaves as expected.

---

## 4. Detailed Walkthrough of Test Cases

### Test Case 1: Standard / Success Case
* **Description**: This test checks if the merge resolution was successful and that the application functions correctly.
* **Inputs**:
  ```json
  {
    "username": "testuser",
    "password": "mypassword",
    "stored_hash": "hashed_password_from_bcrypt"
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The `login` method receives the input values.
  2. It checks if the user is locked out (which evaluates to false).
  3. The `verify_password` method is called, which uses bcrypt to check the password against the stored hash.
  4. If the password is correct, the method generates a JWT token and returns a success response.
* **Expected Output**: 
  ```json
  {
    "success": true,
    "token": "generated_jwt_token"
  }
  ```

### Test Case 2: Edge Case / Validation Fail
* **Description**: This test checks the scenario where the password verification fails.
* **Inputs**:
  ```json
  {
    "username": "testuser",
    "password": "wrongpassword",
    "stored_hash": "hashed_password_from_bcrypt"
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The `login` method receives the input values.
  2. It checks if the user is locked out (which evaluates to false).
  3. The `verify_password` method is called, which uses bcrypt to check the password against the stored hash.
  4. Since the password is incorrect, it records the failure and returns an error response.
* **Expected Output**: 
  ```json
  {
    "success": false,
    "error": "Invalid password. 4 attempts left."
  }
  ```