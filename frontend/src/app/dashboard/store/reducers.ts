import { ProfileState, profileReducer } from "./profile/profile.reducer";


export interface AppState {
    profile: ProfileState
}

export const reducers = {
    profile: profileReducer,
};
