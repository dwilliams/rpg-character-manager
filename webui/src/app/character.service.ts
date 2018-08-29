import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { RPGcharacter } from './rpgcharacter';
import { RPGCHARACTERS } from './mock-rpgcharacters';

import { MessageService } from './message.service';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class CharacterService {
  private charactersUrl = 'api/heroes';  // URL to web api

  constructor(private http: HttpClient, private messageService: MessageService) { }

  getCharacters(): Observable<RPGcharacter[]> {
    return this.http.get<RPGcharacter[]>(this.charactersUrl).pipe(
        tap(characters => this.log('fetched characters')),
        catchError(this.handleError('getCharacters', []))
      );
  }

  getCharacter(id: number): Observable<RPGcharacter> {
    const url = `${this.charactersUrl}/${id}`;
    return this.http.get<RPGcharacter>(url).pipe(
      tap(_ => this.log(`fetched character id=${id}`)),
      catchError(this.handleError<RPGcharacter>(`getCharacter id=${id}`))
    );
  }

  /** PUT: update the character on the server */
  updateCharacter(character: RPGcharacter): Observable<any> {
    return this.http.put(this.charactersUrl, character, httpOptions).pipe(
      tap(_ => this.log(`updated character id=${character.id}`)),
      catchError(this.handleError<any>('updateCharacter'))
    );
  }

  /** POST: add a new character to the server */
  addCharacter(character: RPGcharacter): Observable<RPGcharacter> {
    return this.http.post<RPGcharacter>(this.charactersUrl, character, httpOptions).pipe(
      tap((character: RPGcharacter) => this.log(`added Character w/ id=${character.id}`)),
      catchError(this.handleError<RPGcharacter>('addCharacter'))
    );
  }

  /** DELETE: delete the character from the server */
  deleteCharacter(character: RPGcharacter | number): Observable<RPGcharacter> {
    const id = typeof character === 'number' ? character : character.id;
    const url = `${this.charactersUrl}/${id}`;

    return this.http.delete<RPGcharacter>(url, httpOptions).pipe(
      tap(_ => this.log(`deleted character id=${id}`)),
      catchError(this.handleError<RPGcharacter>('deleteCharacter'))
    );
  }

  /* GET character whose name contains search term */
  searchCharacters(term: string): Observable<RPGcharacter[]> {
    if(!term.trim()) {
      // if not search term, return empty array.
      return of([]);
    }
    return this.http.get<RPGcharacter[]>(`${this.charactersUrl}/?name=${term}`).pipe(
      tap(_ => this.log(`found characters matching "${term}"`)),
      catchError(this.handleError<RPGcharacter[]>('searchCharacters', []))
    );
  }

  private log(message: string) {
    this.messageService.add(`CharacterService: ${message}`);
  }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
 
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead
 
      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);
 
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
