import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';

@Component({
    selector: 'app-profile',
    templateUrl: './profile.component.html'
})
export class ProfileComponent implements OnInit {

    constructor(private authService: AuthService) {
        this.getCookie('your_cookie_name');
    }

    getCookie(name: string): void {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        console.log(parts);
    }

    ngOnInit(): void {
        this.authService.getProfile().subscribe({
            next: result => {
                console.log(result);
            }
        })
    }

}
