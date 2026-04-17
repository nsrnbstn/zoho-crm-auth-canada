# Zoho CRM Canada OAuth Helper

A Python utility to handle the initial OAuth 2.0 handshake for **Zoho Cloud Canada** region. This script helps developers exchange a temporary Grant Token for a permanent Refresh Token.

## 🚀 Purpose
Integrated into the **Amaranth Marketing Agency** internal tools, this script ensures secure, long-term connectivity between custom automation scripts and Zoho CRM.

## 🛠️ Setup
1. Register your client at the [Zoho API Console (.ca)](https://api-console.zohocloud.ca).
2. Generate a `Grant Token` with the required scopes (e.g., `ZohoCRM.modules.ALL`).
3. Replace the placeholder credentials in `zoho_auth.py`.
4. Run the script: `python zoho_auth.py`.

## 🔒 Security Note
Always use environment variables for `CLIENT_SECRET` in production. Never commit active credentials to version control.
