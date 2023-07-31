import { Component } from '@angular/core';
import { AuthService, SignInlink, UserProfile } from '../auth.service';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html'
})
export class LoginComponent {

    loginForm: FormGroup = new FormGroup({
        "email": new FormControl("test@test.com", [Validators.required, Validators.email]),
        "password": new FormControl("test@test.com", [Validators.required]),
    })

    constructor(
        private authService: AuthService,
        private router: Router
    ) { }

    signInWithGoogle() {
        this.authService.googleSignIn().subscribe({
            next: (result: SignInlink) => {
                window.location.href = decodeURIComponent(result.link);
            }
        })
    }

    Submit(): void {
        if (this.loginForm.valid) {
            this.authService.regularLogin(this.loginForm.value).subscribe({
                next: result => {
                    if (result.status) {
                        this.router.navigate(['/auth/profile']);
                    }
                }
            })
        }
    }
}
