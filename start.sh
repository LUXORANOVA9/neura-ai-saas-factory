#!/bin/bash

# NEURA AI SaaS Factory Startup Script
echo "🚀 Starting NEURA AI SaaS Factory..."

# Set environment variables
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
export JWT_SECRET="neura-ai-saas-factory-secret-key-change-in-production"
export STRIPE_SECRET_KEY="sk_test_your_stripe_key_here"

# Create necessary directories
mkdir -p logs
mkdir -p data

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Initialize database
echo "🗄️ Initializing database..."
python -c "
from core.auth.auth_manager import AuthManager
from core.billing.billing_manager import BillingManager
print('Initializing authentication system...')
auth = AuthManager()
print('Initializing billing system...')
billing = BillingManager()
print('Database initialized successfully!')
"

# Start the FastAPI server
echo "🌐 Starting FastAPI server..."
echo "Dashboard will be available at: http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo "SaaS Dashboard: http://localhost:8000/ui/saas-dashboard/"

# Run the server
cd core && python main.py
