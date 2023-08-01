import { createFeatureSelector, createSelector } from "@ngrx/store";
import { ProfileState } from "./profile.reducer";
import { selectState } from "../selectors";
// export const selectAuthState = createFeatureSelector<ProfileState>("profile");

export const selectProfile = createSelector(
    selectState,
    app => app.profile
);


export const selectProfileObj = createSelector(
    selectProfile,
    profile_obj => profile_obj.profile
);