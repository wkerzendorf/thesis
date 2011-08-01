import sqlite3
conn = sqlite3.connect
conn.execute("select name, ra, dec, vrot, vrad "
            "from stars "
            "inner join sparam_laird "
            "   on sparam_laird.star_id=stars.id "
            "inner join vrad_combined "
            "   on vrad_combined.id=stars.id "
            "where name like 'SN1006%'").fetchall()