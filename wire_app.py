import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\App.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Imports
if "AuditLogPage" not in content:
    content = content.replace("import AnalyticsPage from './pages/AnalyticsPage';", "import AnalyticsPage from './pages/AnalyticsPage';\nimport AuditLogPage from './pages/AuditLogPage';\nimport SettingsPage from './pages/SettingsPage';")

# 2. Routes
new_routes = """
      <Route
        path="/audit"
        element={
          <MainLayout>
            <AuditLogPage />
          </MainLayout>
        }
      />
      <Route
        path="/settings"
        element={
          <MainLayout>
            <SettingsPage />
          </MainLayout>
        }
      />
      <Route path="*" element={<Navigate to="/" replace />} />
"""

content = content.replace("<Route path=\"*\" element={<Navigate to=\"/\" replace />} />", new_routes.strip())

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("App.tsx updated.")
