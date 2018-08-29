import { Component, OnInit, Input } from '@angular/core';
import { RPGcharacter } from '../rpgcharacter';

@Component({
  selector: 'app-character-detail',
  templateUrl: './character-detail.component.html',
  styleUrls: ['./character-detail.component.css']
})
export class CharacterDetailComponent implements OnInit {
  @Input() character: RPGcharacter;

  constructor() { }

  ngOnInit() {
  }

}
