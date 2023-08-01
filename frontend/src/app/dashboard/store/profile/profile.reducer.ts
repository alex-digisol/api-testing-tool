import { createReducer, on } from '@ngrx/store';
import { ProfileActions } from './profile.action-types';
import { Profile } from '../../typedefs';


export interface ProfileState {
    profile: Profile | undefined
    error: string | undefined
    loading: boolean
}

export const initialAuthState: ProfileState = {
    profile: undefined,
    error: undefined,
    loading: false
}

export const profileReducer = createReducer(
    initialAuthState,
    on(ProfileActions.getProfileStart, (state, action) => ({ profile: undefined, error: undefined, loading: true })),
    on(ProfileActions.getProfileSuccess, (state, action) => ({ profile: action.payload, error: undefined, loading: false })),
    on(ProfileActions.getProfileError, (state, action) => ({ profile: undefined, error: action.payload, loading: false }))
)