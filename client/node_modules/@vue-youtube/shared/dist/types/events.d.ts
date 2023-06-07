import type { PlayerState, PlayerError } from './enums';
import type { VideoQuality } from './quality';
import type { Player } from './player';
export declare type PlaybackQualityChangeCallback = PlayerEventCallback<PlaybackQualityChangeEvent>;
export declare type PlaybackRateChangeCallback = PlayerEventCallback<PlaybackRateChangeEvent>;
export declare type PlayerStateChangeCallback = PlayerEventCallback<PlayerStateChangeEvent>;
export declare type APIChangeCallback = PlayerEventCallback<PlayerEvent>;
export declare type ReadyCallback = PlayerEventCallback<PlayerEvent>;
export declare type ErrorCallback = PlayerEventCallback<ErrorEvent>;
export interface Events {
    onPlaybackQualityChange?: PlaybackQualityChangeCallback | undefined;
    onPlaybackRateChange?: PlaybackRateChangeCallback | undefined;
    onStateChange?: PlayerStateChangeCallback | undefined;
    onApiChange?: APIChangeCallback | undefined;
    onReady?: ReadyCallback | undefined;
    onError?: ErrorCallback | undefined;
}
export interface PlayerEvent {
    target: Player;
}
export interface PlaybackQualityChangeEvent extends PlayerEvent {
    data: VideoQuality;
}
export interface PlaybackRateChangeEvent extends PlayerEvent {
    data: number;
}
export interface PlayerStateChangeEvent extends PlayerEvent {
    data: PlayerState;
}
export interface ErrorEvent extends PlayerEvent {
    data: PlayerError;
}
export interface PlayerEventCallback<T extends PlayerEvent> {
    (event: T): void;
}
export declare type AnyEvent = PlaybackQualityChangeEvent | PlaybackRateChangeEvent | PlayerStateChangeEvent | PlayerEvent | ErrorEvent;
