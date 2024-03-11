# generated by datamodel-codegen:
#   filename:  test-config.json
#   timestamp: 2024-03-11T13:42:17+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Allowed(BaseModel):
    origins: Optional[List[str]] = None
    headers: Optional[List[str]] = None


class ApiSettings(BaseModel):
    cors: Optional[Cors] = None


class Borders(BaseModel):
    boundaries: Optional[str] = None
    ids: Optional[str] = None
    openborders: Optional[str] = None


class Ch(BaseModel):
    enabled: Optional[bool] = None
    threads: Optional[int] = None
    weightings: Optional[str] = None


class Condition(BaseModel):
    request_service: Optional[str] = None
    request_profile: Optional[str] = None
    request_preference: Optional[str] = None
    api_format: Optional[str] = None
    api_version: Optional[int] = None
    time_after: Optional[str] = None
    time_before: Optional[str] = None


class Core1(BaseModel):
    disabling_allowed: Optional[bool] = None
    active_landmarks: Optional[int] = None


class Core3(Core1):
    pass


class Core5(Core1):
    pass


class Cors(BaseModel):
    allowed: Optional[Allowed] = None
    exposed: Optional[Exposed] = None
    preflight_max_age: Optional[int] = None


class DefaultParams(BaseModel):
    enabled: Optional[bool] = None
    threads: Optional[int] = None
    weightings: Optional[str] = None
    maxcellnodes: Optional[int] = None


class DefaultParams1(BaseModel):
    encoder_flags_size: Optional[int] = None
    graphs_root_path: Optional[str] = None
    elevation_provider: Optional[str] = None
    elevation_cache_clear: Optional[bool] = None
    elevation_cache_path: Optional[str] = None
    elevation_smoothing: Optional[bool] = None
    instructions: Optional[bool] = None
    maximum_distance: Optional[int] = None
    maximum_distance_round_trip_routes: Optional[int] = None
    maximum_segment_distance_with_dynamic_weights: Optional[int] = None
    maximum_waypoints: Optional[int] = None
    maximum_snapping_radius: Optional[int] = None
    maximum_avoid_polygon_area: Optional[int] = None
    maximum_avoid_polygon_extent: Optional[int] = None
    preparation: Optional[Preparation] = None
    execution: Optional[Execution] = None


class Execution(BaseModel):
    methods: Optional[Methods1] = None


class Execution1(BaseModel):
    methods: Optional[Methods3] = None


class Execution2(BaseModel):
    methods: Optional[Methods5] = None


class Execution3(BaseModel):
    methods: Optional[Methods7] = None


class Exposed(BaseModel):
    headers: Optional[List[str]] = None


class ExtStorages(BaseModel):
    WayCategory: Optional[Dict[str, Any]] = None
    HeavyVehicle: Optional[HeavyVehicle] = None
    WaySurfaceType: Optional[Dict[str, Any]] = None
    Tollways: Optional[Dict[str, Any]] = None
    Borders: Optional[Borders] = None
    RoadAccessRestrictions: Optional[RoadAccessRestrictions] = None
    HereTraffic: Optional[HereTraffic] = None


class ExtStorages1(BaseModel):
    WayCategory: Optional[Dict[str, Any]] = None
    HeavyVehicle: Optional[HeavyVehicle] = None
    WaySurfaceType: Optional[Dict[str, Any]] = None
    Tollways: Optional[Dict[str, Any]] = None
    Borders: Optional[Borders] = None


class ExtStorages2(BaseModel):
    WayCategory: Optional[Dict[str, Any]] = None
    WaySurfaceType: Optional[Dict[str, Any]] = None
    HillIndex: Optional[Dict[str, Any]] = None
    TrailDifficulty: Optional[Dict[str, Any]] = None


class ExtStorages6(BaseModel):
    GreenIndex: Optional[GreenIndex] = None
    NoiseIndex: Optional[NoiseIndex] = None
    csv: Optional[Csv] = None
    ShadowIndex: Optional[ShadowIndex] = None
    WayCategory: Optional[Dict[str, Any]] = None
    WaySurfaceType: Optional[Dict[str, Any]] = None
    HillIndex: Optional[Dict[str, Any]] = None
    TrailDifficulty: Optional[Dict[str, Any]] = None


class ExtStorages7(BaseModel):
    GreenIndex: Optional[GreenIndex] = None
    NoiseIndex: Optional[NoiseIndex] = None
    ShadowIndex: Optional[ShadowIndex] = None
    WayCategory: Optional[Dict[str, Any]] = None
    WaySurfaceType: Optional[Dict[str, Any]] = None
    HillIndex: Optional[Dict[str, Any]] = None
    TrailDifficulty: Optional[Dict[str, Any]] = None


class ExtStorages8(BaseModel):
    Wheelchair: Optional[Wheelchair] = None
    WaySurfaceType: Optional[Dict[str, Any]] = None
    WayCategory: Optional[Dict[str, Any]] = None
    OsmId: Optional[Dict[str, Any]] = None


class Fastisochrones(BaseModel):
    maximum_range_distance: Optional[List[MaximumRangeDistanceItem]] = None
    maximum_range_time: Optional[List[MaximumRangeTimeItem]] = None
    profiles: Optional[Profiles] = None


class GreenIndex(BaseModel):
    filepath: Optional[str] = None


class HeavyVehicle(BaseModel):
    restrictions: Optional[bool] = None


class HereTraffic(BaseModel):
    enabled: Optional[bool] = None
    streets: Optional[str] = None
    ref_pattern: Optional[str] = None
    pattern_15min: Optional[str] = None
    radius: Optional[int] = None
    output_log: Optional[bool] = None
    log_location: Optional[str] = None


class Hgv(DefaultParams):
    pass


class Info(BaseModel):
    base_url: Optional[str] = None
    swagger_documentation_url: Optional[str] = None
    support_mail: Optional[str] = None
    author_tag: Optional[str] = None
    content_licence: Optional[str] = None


class Isochrones(BaseModel):
    enabled: Optional[bool] = None
    attribution: Optional[str] = None
    maximum_range_distance: Optional[List[MaximumRangeDistanceItem]] = None
    maximum_range_time: Optional[List[MaximumRangeTimeItem]] = None
    fastisochrones: Optional[Fastisochrones] = None
    maximum_intervals: Optional[int] = None
    maximum_locations: Optional[int] = None
    allow_compute_area: Optional[bool] = None


class KafkaConsumerItem(BaseModel):
    cluster: Optional[str] = None
    topic: Optional[str] = None
    profile: Optional[str] = None


class Lm(BaseModel):
    enabled: Optional[bool] = None
    threads: Optional[int] = None
    weightings: Optional[str] = None
    landmarks: Optional[int] = None


class Lm1(BaseModel):
    active_landmarks: Optional[int] = None


class Lm2(Lm):
    pass


class Lm3(Lm1):
    pass


class Lm4(Lm):
    pass


class Lm5(Lm1):
    pass


class Logging(BaseModel):
    enabled: Optional[bool] = None
    level_file: Optional[str] = None
    location: Optional[str] = None
    stdout: Optional[bool] = None


class Matrix(BaseModel):
    enabled: Optional[bool] = None
    maximum_routes: Optional[int] = None
    maximum_visited_nodes: Optional[int] = None
    allow_resolve_locations: Optional[bool] = None
    attribution: Optional[str] = None


class MaximumRangeDistanceItem(BaseModel):
    profiles: Optional[str] = None
    value: Optional[int] = None


class MaximumRangeTimeItem(MaximumRangeDistanceItem):
    pass


class Methods(BaseModel):
    lm: Optional[Lm] = None


class Methods1(BaseModel):
    lm: Optional[Lm1] = None


class Methods2(BaseModel):
    ch: Optional[Ch] = None
    lm: Optional[Lm2] = None
    core: Optional[Core] = None


class Methods3(BaseModel):
    lm: Optional[Lm3] = None
    core: Optional[Core1] = None


class Methods4(BaseModel):
    ch: Optional[Ch] = None
    lm: Optional[Lm4] = None
    core: Optional[Core2] = None


class Methods5(BaseModel):
    lm: Optional[Lm5] = None
    core: Optional[Core3] = None


class Methods6(BaseModel):
    core: Optional[Core4] = None


class Methods7(BaseModel):
    core: Optional[Core5] = None


class NoiseIndex(GreenIndex):
    pass


class Ors(BaseModel):
    info: Optional[Info] = None
    api_settings: Optional[ApiSettings] = None
    services: Optional[Services] = None
    logging: Optional[Logging] = None
    kafka_test_cluster: Optional[bool] = None
    kafka_consumer: Optional[List[KafkaConsumerItem]] = None
    system_message: Optional[List[SystemMessageItem]] = None


class OrsConfigJSON(BaseModel):
    ors: Optional[Ors] = None


class Parameters(BaseModel):
    encoder_options: Optional[str] = None
    maximum_distance: Optional[int] = None
    elevation: Optional[bool] = None
    preparation: Optional[Preparation1] = None
    execution: Optional[Execution1] = None
    ext_storages: Optional[ExtStorages] = None
    traffic: Optional[bool] = None


class Parameters1(BaseModel):
    encoder_options: Optional[str] = None
    maximum_distance: Optional[int] = None
    elevation: Optional[bool] = None
    maximum_speed_lower_bound: Optional[int] = None
    preparation: Optional[Preparation2] = None
    execution: Optional[Execution2] = None
    ext_storages: Optional[ExtStorages1] = None
    traffic: Optional[bool] = None


class Parameters2(BaseModel):
    encoder_options: Optional[str] = None
    elevation: Optional[bool] = None
    preparation: Optional[Preparation3] = None
    execution: Optional[Execution3] = None
    ext_storages: Optional[ExtStorages2] = None


class Parameters3(BaseModel):
    encoder_options: Optional[str] = None
    elevation: Optional[bool] = None
    maximum_snapping_radius: Optional[int] = None
    ext_storages: Optional[ExtStorages2] = None


class Parameters4(BaseModel):
    encoder_options: Optional[str] = None
    elevation: Optional[bool] = None
    ext_storages: Optional[ExtStorages2] = None


class Parameters5(Parameters4):
    pass


class Parameters6(BaseModel):
    encoder_options: Optional[str] = None
    elevation: Optional[bool] = None
    interpolate_bridges_and_tunnels: Optional[bool] = None
    ext_storages: Optional[ExtStorages6] = None


class Parameters7(BaseModel):
    encoder_options: Optional[str] = None
    elevation: Optional[bool] = None
    elevation_smoothing: Optional[bool] = None
    ext_storages: Optional[ExtStorages7] = None


class Parameters8(BaseModel):
    encoder_options: Optional[str] = None
    elevation: Optional[bool] = None
    maximum_snapping_radius: Optional[int] = None
    ext_storages: Optional[ExtStorages8] = None


class Parameters9(BaseModel):
    encoder_options: Optional[str] = None
    elevation: Optional[bool] = None
    maximum_visited_nodes: Optional[int] = None
    gtfs_file: Optional[str] = None


class Preparation(BaseModel):
    min_network_size: Optional[int] = None
    min_one_way_network_size: Optional[int] = None
    methods: Optional[Methods] = None


class Preparation1(BaseModel):
    min_network_size: Optional[int] = None
    min_one_way_network_size: Optional[int] = None
    methods: Optional[Methods2] = None


class Preparation2(BaseModel):
    min_network_size: Optional[int] = None
    min_one_way_network_size: Optional[int] = None
    methods: Optional[Methods4] = None


class Preparation3(BaseModel):
    min_network_size: Optional[int] = None
    min_one_way_network_size: Optional[int] = None
    methods: Optional[Methods6] = None


class ProfileBikeElectric(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters5] = None


class ProfileBikeMountain(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters3] = None


class ProfileBikeRegular(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters2] = None


class ProfileBikeRoad(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters4] = None


class ProfileCar(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters] = None


class ProfileHgv(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters1] = None


class ProfileHiking(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters7] = None


class ProfilePublicTransport(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters9] = None


class ProfileWalking(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters6] = None


class ProfileWheelchair(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters8] = None


class Profiles(BaseModel):
    default_params: Optional[DefaultParams] = None
    hgv: Optional[Hgv] = None


class Profiles1(BaseModel):
    active: Optional[List[str]] = None
    default_params: Optional[DefaultParams1] = None
    profile_car: Optional[ProfileCar] = Field(None, alias='profile-car')
    profile_hgv: Optional[ProfileHgv] = Field(None, alias='profile-hgv')
    profile_bike_regular: Optional[ProfileBikeRegular] = Field(
        None, alias='profile-bike-regular'
    )
    profile_bike_mountain: Optional[ProfileBikeMountain] = Field(
        None, alias='profile-bike-mountain'
    )
    profile_bike_road: Optional[ProfileBikeRoad] = Field(
        None, alias='profile-bike-road'
    )
    profile_bike_electric: Optional[ProfileBikeElectric] = Field(
        None, alias='profile-bike-electric'
    )
    profile_walking: Optional[ProfileWalking] = Field(None, alias='profile-walking')
    profile_hiking: Optional[ProfileHiking] = Field(None, alias='profile-hiking')
    profile_wheelchair: Optional[ProfileWheelchair] = Field(
        None, alias='profile-wheelchair'
    )
    profile_public_transport: Optional[ProfilePublicTransport] = Field(
        None, alias='profile-public-transport'
    )


class RoadAccessRestrictions(BaseModel):
    use_for_warnings: Optional[bool] = None


class Routing(BaseModel):
    enabled: Optional[bool] = None
    mode: Optional[str] = None
    routing_description: Optional[str] = None
    routing_name: Optional[str] = None
    sources: Optional[List[str]] = None
    init_threads: Optional[int] = None
    attribution: Optional[str] = None
    distance_approximation: Optional[bool] = None
    elevation_preprocessed: Optional[bool] = None
    profiles: Optional[Profiles1] = None


class Services(BaseModel):
    matrix: Optional[Matrix] = None
    isochrones: Optional[Isochrones] = None
    routing: Optional[Routing] = None


class ShadowIndex(GreenIndex):
    pass


class SystemMessageItem(BaseModel):
    active: Optional[bool] = None
    text: Optional[str] = None
    condition: Optional[Condition] = None


class Wheelchair(BaseModel):
    KerbsOnCrossings: Optional[str] = None


class Core(Lm):
    pass


class Core2(Lm):
    pass


class Core4(Lm):
    pass


class Csv(GreenIndex):
    pass
