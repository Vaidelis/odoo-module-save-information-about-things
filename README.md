# Save Information Odoo Module

## Overview

This Odoo module, `save_information`, is designed to manage and save information related to various entities. It provides a data model, views, and security groups to facilitate the storage and retrieval of information.

## Features

- **Information Model (`save_information.save_information`):**
  - Fields:
    - `name`: Name of the information (Required).
    - `description`: Description of the information.
    - `company_id`: Reference to the company associated with the information (Required).

- **Security Groups:**
  - `group_saveinformation_manager`: Group for managing saved information.

- **Views:**
  - **Form View (`save_information.save_information_form_view`):**
    - Provides a form for creating and editing information.
  - **Tree View (`save_information.save_information_tree_view`):**
    - Displays information in a tree structure.
  - **Search View (`save_information.save_information_search_view`):**
    - Enables searching for information based on name, description, and company.
  
- **Menu and Actions:**
  - **Action (`save_information.save_information_list_action`):**
    - Defines an action for displaying the list of saved information in both tree and form views.
  - **Menu Items:**
    - Main Menu (`main_saveinformation_menu`): "Information Portfolio" accessible to users in the `group_saveinformation_manager` group.
    - Sub-menu (`saveinformation_menu`): "Menu" under the main menu.
    - Sub-menu (`information_portfolio`): "Information Portfolio" under the "Menu," linked to the action.

## Installation

1. Copy the `save_information` folder to your Odoo addons directory.
2. Update the Odoo module list to include the new module.
3. Install and update the module using the Odoo interface or command line.

## Usage

1. Navigate to the "Information Portfolio" menu.
2. Create, edit, and view information records using the provided views.

## Security

- The module includes a security group (`group_saveinformation_manager`) to control access to information management features.

## Credits

- This module was created by Vaidas.
