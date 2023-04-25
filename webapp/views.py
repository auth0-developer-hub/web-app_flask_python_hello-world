from flask import Blueprint, render_template, session

from services.message_service import MessageService
from auth.decorators import requires_auth

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
@requires_auth
def profile():
    """
    Unprotected endpoint which displays your profile if you are logged in, otherwise it prompts the user to log in
    """
    return render_template('profile.html', user_profile=session.get('user').get("userinfo"))


@webapp_bp.route("/protected")
@requires_auth
def protected():
    """
    Unprotected endpoint which displays your profile if you are logged in, otherwise it prompts the user to log in
    """
    return render_template('protected.html', message=MessageService().protected_message())


@webapp_bp.route("/admin")
@requires_auth
def admin():
    """
    Unprotected endpoint which displays your profile if you are logged in, otherwise it prompts the user to log in
    """
    return render_template('admin.html', message=MessageService().admin_message())