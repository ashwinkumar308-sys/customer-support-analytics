import sqlite3

conn = sqlite3.connect("workload.db")
cursor = conn.cursor()

# Tickets per agent
cursor.execute("""
SELECT agent_name, COUNT(*) FROM tickets GROUP BY agent_name
""")
print("Tickets per agent:", cursor.fetchall())

# Avg resolution time
cursor.execute("""
SELECT agent_name, AVG(resolution_time) FROM tickets GROUP BY agent_name
""")
print("Avg resolution time:", cursor.fetchall())

# Team workload
cursor.execute("""
SELECT team, COUNT(*) FROM tickets GROUP BY team
""")
print("Workload per team:", cursor.fetchall())