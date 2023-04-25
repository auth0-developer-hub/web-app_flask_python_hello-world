from flask import Blueprint, render_template

from services.message_service import MessageService

webapp_bp = Blueprint('webapp', __name__, template_folder="templates")


@webapp_bp.route("/")
def home():
    """
    Home endpoint
    """
    features = [{
        "title": "Identity Providers",
        "description":
            "Auth0 supports social providers such as Google, Facebook, and Twitter, along with Enterprise providers "
            "such as Microsoft Office 365, Google Apps, and Azure. You can also use any OAuth 2.0 Authorization "
            "Server.",
        "resourceUrl": "https://auth0.com/docs/connections",
        "icon": "https://cdn.auth0.com/blog/hello-auth0/identity-providers-logo.svg",
    }, {
        "title": "Multi-Factor Authentication",
        "description":
            "You can require your users to provide more than one piece of identifying information when logging in. "
            "MFA delivers one-time codes to your users via SMS, voice, email, WebAuthn, and push notifications.",
        "resourceUrl": "https://auth0.com/docs/multifactor-authentication",
        "icon": "https://cdn.auth0.com/blog/hello-auth0/mfa-logo.svg",
    }, {
        "title": "Attack Protection",
        "description":
            "Auth0 can detect attacks and stop malicious attempts to access your application such as blocking traffic "
            "from certain IPs and displaying CAPTCHA. Auth0 supports the principle of layered protection in security "
            "that uses a variety of signals to detect and mitigate attacks.",
        "resourceUrl": "https://auth0.com/docs/attack-protection",
        "icon": "https://cdn.auth0.com/blog/hello-auth0/advanced-protection-logo.svg",
    }, {
        "title": "Serverless Extensibility",
        "description":
            "Actions are functions that allow you to customize the behavior of Auth0. Each action is bound to a "
            "specific triggering event on the Auth0 platform. Auth0 invokes the custom code of these Actions when the "
            "corresponding triggering event is produced at runtime.",
        "resourceUrl": "https://auth0.com/docs/actions",
        "icon": "https://cdn.auth0.com/blog/hello-auth0/private-cloud-logo.svg",
    }]

    return render_template("home.html", features=features)


@webapp_bp.route("/public")
def public():
    return render_template('public.html', message=MessageService().public_message())


@webapp_bp.route("/profile")
def profile():
    """
    Unprotected endpoint which displays your profile if you are logged in, otherwise it prompts the user to log in
    """
    user_profile = {
        "nickname": "Customer",
        "name": "One Customer",
        "picture": "https://cdn.auth0.com/blog/hello-auth0/auth0-user.png",
        "updated_at": "2021-05-04T21:33:09.415Z",
        "email": "customer@example.com",
        "email_verified": False,
        "sub": "auth0|12345678901234567890"
    }

    return render_template('profile.html', user_profile=user_profile)


@webapp_bp.route("/protected")
def protected():
    """
    Unprotected endpoint which displays your profile if you are logged in, otherwise it prompts the user to log in
    """
    return render_template('protected.html', message=MessageService().protected_message())


@webapp_bp.route("/admin")
def admin():
    """
    Unprotected endpoint which displays your profile if you are logged in, otherwise it prompts the user to log in
    """
    return render_template('admin.html', message=MessageService().admin_message())