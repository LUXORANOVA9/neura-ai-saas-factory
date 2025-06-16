# 🚀 NEURA AI SaaS Factory

**Automated AI SaaS services with API key monetization**

A complete, production-ready SaaS platform that automatically generates and monetizes AI services through API keys, subscriptions, and one-time payments.

## 🌟 Features

### 🤖 AI Services
- **Resume Reviewer** - AI-powered resume analysis and optimization ($9.99-$29.99)
- **Landing Page Generator** - Create stunning landing pages with AI ($29.99-$99.99)
- **Name/Brand Generator** - Generate creative business names ($19.99-$79.99)
- **SEO Audit Bot** - Comprehensive website SEO analysis ($29.99-$99.99)
- **Logo Maker** - AI-generated professional logos ($39.99-$149.99)

### 💳 Monetization Features
- **API Key Authentication** - Secure access control
- **Subscription Plans** - Free, Starter ($29.99), Professional ($99.99), Enterprise ($299.99)
- **Usage Tracking** - Monitor API calls and enforce limits
- **Stripe Integration** - Secure payment processing
- **Billing Management** - Automated subscription handling

### 📊 Dashboard & Analytics
- **Modern SaaS Dashboard** - Beautiful Tailwind CSS interface
- **Real-time Analytics** - Usage stats, revenue tracking
- **User Management** - Registration, authentication, API keys
- **Service Modals** - Interactive service testing

## 🏗️ Architecture

```
neura-ai-saas-factory/
├── core/
│   ├── auth/
│   │   └── auth_manager.py      # Authentication & API key management
│   ├── billing/
│   │   └── billing_manager.py   # Subscriptions & payments
│   ├── products/
│   │   └── ai_services.py       # AI service implementations
│   └── main.py                  # FastAPI application
├── ui/
│   └── saas-dashboard/
│       └── index.html           # Modern SaaS dashboard
├── requirements.txt             # Dependencies
├── start.sh                     # Startup script
└── README.md                    # This file
```

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <repository-url>
cd neura-ai-saas-factory
chmod +x start.sh
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
```bash
export JWT_SECRET="your-secret-key"
export STRIPE_SECRET_KEY="sk_test_your_stripe_key"
```

### 4. Start the Application
```bash
./start.sh
```

### 5. Access the Platform
- **Dashboard**: http://localhost:8000/dashboard
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📚 API Usage

### Authentication
```bash
# Register new user
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'

# Response includes API key
{
  "message": "User registered successfully",
  "user_id": 1,
  "api_key": "neura_abc123...",
  "email": "user@example.com"
}
```

### Using AI Services
```bash
# Resume Review
curl -X POST http://localhost:8000/api/resume/review \
  -H "Authorization: Bearer neura_abc123..." \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "Your resume content...",
    "job_description": "Target job description..."
  }'

# Landing Page Generation
curl -X POST http://localhost:8000/api/landing-page/generate \
  -H "Authorization: Bearer neura_abc123..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "TechFlow Solutions",
    "industry": "Technology",
    "target_audience": "Small Businesses",
    "benefits": ["Automated Workflows", "Cost Reduction", "24/7 Support"]
  }'
```

### Billing & Subscriptions
```bash
# Get pricing plans
curl http://localhost:8000/billing/plans

# Check usage
curl http://localhost:8000/billing/usage \
  -H "Authorization: Bearer neura_abc123..."
```

## 💰 Pricing Plans

| Plan | Price | Monthly Requests | Features |
|------|-------|------------------|----------|
| **Free** | $0 | 100 | Basic API access, Email support |
| **Starter** | $29.99 | 5,000 | All AI services, Priority support |
| **Professional** | $99.99 | 25,000 | 24/7 support, Custom integrations |
| **Enterprise** | $299.99 | 100,000 | Dedicated support, SLA guarantee |

## 🛠️ Technology Stack

- **Backend**: FastAPI, Python 3.10+
- **Database**: SQLite (production: PostgreSQL)
- **Authentication**: JWT, API Keys
- **Payments**: Stripe
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **AI Services**: OpenAI, Transformers, Custom algorithms
- **Deployment**: Docker, Uvicorn

## 🔧 Configuration

### Environment Variables
```bash
# Security
JWT_SECRET="your-jwt-secret-key"
JWT_ALGORITHM="HS256"
JWT_EXPIRE_HOURS=24

# Stripe
STRIPE_SECRET_KEY="sk_test_..."
STRIPE_PUBLISHABLE_KEY="pk_test_..."

# Database
DATABASE_URL="sqlite:///./neura_saas.db"

# AI Services
OPENAI_API_KEY="sk-..."
```

### Database Schema
The application automatically creates the following tables:
- `users` - User accounts and authentication
- `api_keys` - API key management and tracking
- `subscriptions` - User subscription plans
- `payments` - Payment history and transactions
- `monthly_usage` - Usage tracking and billing
- `api_usage_logs` - Detailed API call logs

## 📈 Monitoring & Analytics

### Built-in Analytics
- Real-time usage tracking
- Revenue monitoring
- User engagement metrics
- API performance stats
- Error rate monitoring

### Dashboard Features
- Interactive service testing
- Usage visualization
- Billing history
- Subscription management
- API key generation

## 🔒 Security Features

- **JWT Authentication** - Secure token-based auth
- **API Key Management** - Granular access control
- **Rate Limiting** - Usage-based throttling
- **Input Validation** - Pydantic model validation
- **CORS Protection** - Cross-origin request security
- **SQL Injection Prevention** - Parameterized queries

## 🚀 Deployment

### Docker Deployment
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Considerations
- Use PostgreSQL for production database
- Set up Redis for caching and sessions
- Configure proper SSL certificates
- Set up monitoring with Prometheus/Grafana
- Use environment-specific configuration files
- Implement proper logging and error tracking

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Documentation**: http://localhost:8000/docs
- **Issues**: Create an issue on GitHub
- **Email**: support@neura-ai.com

## 🎯 Roadmap

### Phase 1 (Current)
- ✅ Core AI services implementation
- ✅ Authentication and API key system
- ✅ Stripe payment integration
- ✅ Modern SaaS dashboard
- ✅ Usage tracking and analytics

### Phase 2 (Next)
- [ ] Advanced AI model integration
- [ ] Webhook system for real-time updates
- [ ] Multi-tenant architecture
- [ ] Advanced analytics and reporting
- [ ] Mobile app development

### Phase 3 (Future)
- [ ] White-label solutions
- [ ] Marketplace for custom AI services
- [ ] Enterprise SSO integration
- [ ] Advanced workflow automation
- [ ] AI model training platform

---

**Built with ❤️ by the NEURA AI Team**

*Transform your ideas into profitable AI SaaS products in minutes, not months.*
