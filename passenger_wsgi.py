# Dependencies
import sys
sys.path.append('/home/dldwvxqr/all_domains/fuckthisguyjeff.com/config') 

from flask import Flask, render_template
import pymysql.cursors
import random
import config

application = Flask(__name__)
application.debug = True

@application.route("/")
def main():
    # Set Database connection string
    connection = pymysql.connect(host='localhost',
                                user=config.user,
                                password=config.password,
                                db=config.db,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    
    # Bring back random record from quote table
    sql = 'select * from ftgj_quotes order by rand() limit 1'

    # Parse resulting data
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()
        # Pass returned quote to html template file
        return render_template('index.htm', data=result['quote'])

    connection.close()


if __name__ == "__main__":
    application.run()


 