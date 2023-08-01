import { Injectable } from "@angular/core";
import { createEffect, Actions, ofType } from "@ngrx/effects";
import { ProfileService } from "../../services/profile.service";
import { ProfileActions } from "./profile.action-types";
import { catchError, exhaustMap, map, of } from "rxjs";
import { Profile } from "../../typedefs";
import { Router } from "@angular/router";


@Injectable()
export class ProfileEffects {
    
    constructor(
        private action$: Actions,
        private router: Router,
        private profileService: ProfileService
    ) { }

    userStart$ = createEffect(() => this.action$.pipe(
        ofType(ProfileActions.getProfileStart),
        exhaustMap(() =>
            this.profileService.getProfile().pipe(
                map((user: Profile) => ProfileActions.getProfileSuccess({ payload: user })),
                catchError(error => {
                    this.router.navigate(["/auth"]);
                    return of(ProfileActions.getProfileError({payload: "Unable to get user"}))
                })
            )
        )
    ));

    userSucces$ = createEffect(() => this.action$.pipe(
        ofType(ProfileActions.getProfileSuccess)
    ), { dispatch: false });

}