# Online Waste Management System

## Description
The **Online Waste Management System** is a Django-based web application that allows users to manage and schedule waste pickups in an organized and efficient way. The system comprises three main modules: User, Admin (Site Handlers), and Waste Pickup Staff, each with distinct features. The project aims to streamline waste management by offering users the ability to categorize their waste and schedule pickups, while allowing admins and staff to manage and track waste collection.

## Technologies Used
- **Language:** Python
- **Framework:** Django
- **Database:** MySQL
- **Front-end:** HTML, CSS, JavaScript
- **Payment Gateway:** Razorpay

## Modules

### 1. User Module
- **User Dashboard:** Each user has a personal dashboard after account creation.
  ![User Dashboard](https://github.com/AbhayBS85/Waste_management-_project/blob/194aa300b41596973d7ace37f6353f190d4f88a6/screenshots/homepage.jpg)
- **Waste Donation:** Users can donate waste by categorizing it into:
  - Bio-degradable waste
  - Non-bio-degradable waste
  - Hazardous waste
 
    ![waste category](https://github.com/AbhayBS85/Waste_management-_project/blob/2befb41d48645c283b43f13f872d586c7aa562e8/screenshots/waste_category.jpg)
- **Waste Pickup Scheduling:** Users can schedule a pickup and select the type of waste they are donating.

  ![pickup scheduling](https://github.com/AbhayBS85/Waste_management-_project/blob/c9f0234148f37bf189fe48eeb989e073c08c3ef2/screenshots/scheduling_pickup.jpg)
- **Profile Management:** Users can update personal information like phone number and email, but the username remains uneditable after account creation.
- **Payment Options:** Users can choose between online payment (integrated via Razorpay) or payment upon pickup.

  ![payment gateway](https://github.com/AbhayBS85/Waste_management-_project/blob/61e1603646ef0f1a6ed51b04e058a707a2141f4c/screenshots/payment_gateway.jpg)

### 2. Admin (Site Handlers) Module
- **Pickup Management:** Admins can view all scheduled pickups and manage them efficiently. Each pickup request is assigned a unique ID and is displayed in reverse chronological order (most recent first).

  ![pickup view](https://github.com/AbhayBS85/Waste_management-_project/blob/09cd03d4bb7c5cce50a0f2b3a6dc5adc98189902/screenshots/latest_pickup.jpg)
- **Assign Staff:** Admins can assign available staff to handle pickups. Available staff are displayed in a table format, and the admin can select the staff member for each task.
- **Staff Management:** Admins can:
  - Add new staff members
  - Edit existing staff details
  - Delete staff members
- **Pickup Tracking:** Admins can monitor pickups, divided into two categories:
  - **Assigned Pickups:** Tasks that have been assigned to staff.
  - **Finished Pickups:** Tasks completed by staff.

### 3. Waste Pickup Staff Module
- **Pickup Assignment:** Staff members can confirm and accept pickups assigned by the admin.
- **Complete Pickup:** After finishing the pickup task, staff members can mark the task as completed.
- **Pickup History:** Each staff member has a personal dashboard where they can view the history of their completed pickups.

  ![previous pickups](https://github.com/AbhayBS85/Waste_management-_project/blob/701690db614f2689504e55ec360a4263e55f4b47/screenshots/previous%20pickups.jpg)
- **Update Availability Status:** Staff members can update their status to indicate whether they are:
  - **"Free to Pick":** Available to accept new pickups.
  - **"Busy":** Not available for new pickups until current tasks are completed.




### Features:

  - **User Features:**
    - Waste donation and categorization
    - Pickup scheduling
    - Personal profile management
    - Payment integration (Razorpay)
    
  - **Admin Features:**
    - View and manage scheduled pickups
    - Assign staff to pickups
    - Add, edit, and delete staff details
    
  - **Staff Features:**
    - Update the status   
    - Confirm and accept assigned pickups
    - Complete pickup tasks
    - View personal pickup history


    
### Payment Integration:
  - The system uses Razorpay for online payment processing. Users can pay online when scheduling a waste pickup or choose to pay in cash upon pickup.

### How it Works

  - **User Workflow:**
    - Sign up and log in.
    - Choose the type of waste and schedule a pickup.
    - Select the preferred payment option.
    - Manage personal details from the dashboard.
    
  - **Admin Workflow:**
    - View new pickup requests.
    - Assign available staff to handle pickups.
    - Manage staff details (add, edit, delete).
  
  - **Staff Workflow:**
    - Confirm the pickup assignment.
    - Mark the pickup as completed after collecting the waste.
    - Review the history of pickups.



