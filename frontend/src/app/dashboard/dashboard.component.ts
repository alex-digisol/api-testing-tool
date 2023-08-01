import { Component, OnInit } from '@angular/core';
import { Store, select } from '@ngrx/store';
import { ProfileState } from './store/profile/profile.reducer';
import { selectProfile } from './store/profile/profile.selectors';
import { ProfileActions } from './store/profile/profile.action-types';

@Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html'
})
export class DashboardComponent implements OnInit {
    constructor(private store: Store<ProfileState>) {}

    ngOnInit(): void {
        this.store.dispatch(ProfileActions.getProfileStart());
        // this.store.pipe(select(selectProfile)).subscribe({
        //     next: result => {
        //         console.log(result);
        //     }
        // });
    }
}
