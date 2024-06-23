from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2

from market import app



if __name__ == '__main__':
    app.run(
        debug=True
    )
