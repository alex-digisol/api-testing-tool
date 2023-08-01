import { Component, OnInit } from '@angular/core';
import { ProfileState } from '../../store/profile/profile.reducer';
import { Store } from '@ngrx/store';
import { selectProfileObj } from '../../store/profile/profile.selectors';
import { Profile } from '../../typedefs';
import { Observable } from 'rxjs';

@Component({
    selector: 'app-header',
    templateUrl: './header.component.html'
})
export class HeaderComponent implements OnInit {

    profile$: Observable<Profile|undefined>;

    constructor(private store: Store<ProfileState>) {
        this.profile$ = this.store.select(selectProfileObj);
    }

    ngOnInit(): void {

    }
}
