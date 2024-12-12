from flask import Blueprint, render_template, request, jsonify
from database.db import session
from database.models import TestResults
from datetime import datetime, timedelta, timezone

speed_bp=Blueprint("speed", __name__)

@speed_bp.route("/")
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 25
    total_results = session.query(TestResults).count()
    results = session.query(TestResults).order_by(TestResults.date_test.desc()).offset((page-1) * per_page).limit(per_page).all()
    total_pages = (total_results + per_page - 1) // per_page
    has_next = page < total_pages
    has_previous = page > 1

    return render_template('index.html', results=results, page=page, total_pages=total_pages, has_next=has_next, has_previous=has_previous)

@speed_bp.route("/speed_chart")
def speed_chart():
    return render_template('speed_chart.html')

@speed_bp.route("/api/speedtest_results")
def speedtest_results():
    time_range = request.args.get('time_range', '24h')
    now = datetime.now(timezone.utc)
    if time_range == '24h':
        start_time = now - timedelta(hours=24)
    elif time_range == '7d':
        start_time = now - timedelta(days=7)
    elif time_range == '1m':
        start_time = now - timedelta(days=30)
    elif time_range == '3m':
        start_time = now - timedelta(days=90)
    elif time_range == '6m':
        start_time = now - timedelta(days=180)
    elif time_range == '1y':
        start_time = now - timedelta(days=365)
    else:
        start_time = now - timedelta(hours=24)

    results = session.query(TestResults).filter(TestResults.date_test >= start_time).order_by(TestResults.date_test).all()
    data = {
        'dates': [result.date_test.strftime('%Y-%m-%dT%H:%M:%SZ') for result in results],
        'download_speeds': [result.download_speed for result in results],
        'upload_speeds': [result.upload_speed for result in results]
    }
    return jsonify(data)

@speed_bp.route("/latency_chart")
def latency_chart():
    return render_template('latency_chart.html')

@speed_bp.route('/api/latency_results')
def latency_results():
    time_range = request.args.get('time_range', '24h')
    now = datetime.now(timezone.utc)
    if time_range == '24h':
        start_time = now - timedelta(hours=24)
    elif time_range == '7d':
        start_time = now - timedelta(days=7)
    elif time_range == '1m':
        start_time = now - timedelta(days=30)
    elif time_range == '3m':
        start_time = now - timedelta(days=90)
    elif time_range == '6m':
        start_time = now - timedelta(days=180)
    elif time_range == '1y':
        start_time = now - timedelta(days=365)
    else:
        start_time = now - timedelta(hours=24)

    results = session.query(TestResults).filter(TestResults.date_test >= start_time).order_by(TestResults.date_test).all()
    data = {
        'dates': [result.date_test.strftime('%Y-%m-%dT%H:%M:%SZ') for result in results],
        'latencies': [result.latency for result in results]
    }
    return jsonify(data)