"""
Quick script to generate a new Django SECRET_KEY for production.
Run this before deploying to production and use the output as your SECRET_KEY environment variable.
"""
from django.core.management.utils import get_random_secret_key

if __name__ == '__main__':
    secret_key = get_random_secret_key()
    print("\n" + "="*60)
    print("Generated SECRET_KEY for production:")
    print("="*60)
    print(secret_key)
    print("="*60)
    print("\n⚠️  IMPORTANT: Keep this secret key secure!")
    print("Add it as an environment variable in your hosting platform.")
    print("="*60 + "\n")

