import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { ProfileState } from './store/profile/profile.reducer';
import { ProfileActions } from './store/profile/profile.action-types';

@Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html'
})
export class DashboardComponent implements OnInit {
    constructor(private store: Store<ProfileState>) {}

    ngOnInit(): void {
        this.store.dispatch(ProfileActions.getProfileStart());
    }
}
