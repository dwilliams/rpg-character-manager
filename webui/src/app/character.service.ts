import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { RPGcharacter } from './rpgcharacter';
import { RPGCHARACTERS } from './mock-rpgcharacters';

import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class CharacterService {
  constructor(private messageService: MessageService) { }

  getCharacters(): Observable<RPGcharacter[]> {
    // TODO: Send this message _after_ fetching the characters
    this.messageService.add('CharacterService: fetched characters');
    return of(RPGCHARACTERS);
  }
}
