import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, shareReplay } from 'rxjs';
import { Profile } from '../typedefs';


@Injectable()
export class ProfileService {

    constructor(private http: HttpClient) { }

    getProfile(): Observable<Profile> {
        return this.http.get<Profile>("/api/v1/auth/profile").pipe(
            shareReplay()
        )
    }

}
