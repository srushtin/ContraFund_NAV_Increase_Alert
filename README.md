# Mutual Fund Daily NAV Alert

An automated Python tool running via **GitHub Actions** that tracks daily Net Asset Value (NAV) updates for Indian mutual funds using the public [mfapi.in](https://www.mfapi.in/) API. 

Whenever the latest NAV is higher than the previous day's value, it sends an email notification containing the current NAV, 1-year high, and historical values for the last 30 days.

---

## Features

- **Automated Daily Runs:** Scheduled via GitHub Actions cron job every day at 11:00 AM IST (`05:30 UTC`).
- **Condition-Based Alerts:** Sends an email only when the NAV increases compared to the previous trading day.
- **Historical Context:** Includes:
  - Current NAV vs. Previous NAV
  - 1-Year High (calculated from the last 365 recorded data points)
  - Date-wise NAV log for the last 30 days
- **Lightweight & Free:** Built with zero server overhead using GitHub Actions and free Gmail SMTP.

---

## How It Works

1. Queries the free `https://api.mfapi.in/mf/{scheme_code}` endpoint.
2. Extracts latest records (`data[0]` for current, `data[1]` for previous).
3. Compares values; if `current_nav > earlier_nav`, connects to Gmail SMTP over TLS.
4. Dispatches a formatted notification email to inbox.

---

## Setup & Configuration

### 1. Gmail App Password
To send emails via Python:
1. Go to your [Google Account Security](https://myaccount.google.com/security).
2. Enable **2-Step Verification** (if not already enabled).
3. Generate an **App Password** (Select App: *Mail*, Device: *Other/GitHub Actions*).
4. Save the generated 16-character password.

### 2. GitHub Secrets
In your GitHub repository, navigate to **Settings** > **Secrets and variables** > **Actions** and add two repository secrets:

| Secret Name | Description |
| :--- | :--- |
| `EMAIL` | Your sender/receiver Gmail address |
| `PWD` | The 16-character Google App Password |

### 3. Change Mutual Fund Scheme (Optional)
By default, the script tracks scheme code `119835`. To track a different fund:
1. Search your mutual fund on [mfapi.in](https://www.mfapi.in/).
2. Locate the numeric scheme code in the URL.
3. Update `scheme_code` in `main.py`:
   ```python
   scheme_code = <YOUR_SCHEME_CODE>