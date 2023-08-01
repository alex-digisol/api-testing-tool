import { createFeatureSelector, createSelector } from "@ngrx/store";
import { ProfileState } from "./profile.reducer";

export const selectAuthState = createFeatureSelector<ProfileState>("profile");

export const selectProfile = createSelector(
    selectAuthState,
    profile => {
        console.log(profile)
        return profile.profile
    }
);